import pymysql
import json
import logging

sql_configuration_file = 'mysql.conf'

def db_conn():
    with open(sql_configuration_file) as conf_file:
        confStr = conf_file.read()
    conf = json.JSONDecoder().decode(confStr)
    host = conf['database']['host']
    user = conf['database']['user']
    password = conf['database']['password']
    db = conf['database']['database_name']
    port = conf['database']['port']
    #connect
    logging.info("connect to db: host:%s, user:%s, password:%s, db:%s, port:%s" % \
        (conf['database']['host'], \
         conf['database']['user'], \
         conf['database']['password'], \
         conf['database']['database_name'], \
         conf['database']['port']))

    connection = pymysql.connect(host=host,
                     user=user,
                     password=password,
                     db=db,
                     port=port)
    return connection

def db_disconn(connection):
    connection.close()

def add_mission(mission_name, trigger_time):
    connection = db_conn()
    try:
        with connection.cursor() as cursor:
            sql ="insert into mission_table (mission_name, trigger_time) values(%s, %s);"
            logging.info("sql request: " + sql)
            try:
                cursor.execute(sql, (mission_name, trigger_time))
                connection.commit()
                return True
            except:
                print("database operation fail")
                connection.rollback();
                return False
    finally:
        db_disconn(connection);
        
def modify_mission(id, mission_name, trigger_time):
    #situtation have to be verify: no target mission
    connection = db_conn()
    try:
        with connection.cursor() as cursor:
            modify_sql = "update mission_table set mission_name='%s',trigger_time='%s' where id=%d" % (mission_name, trigger_time, id)
            logging.info("modify sql: " + modify_sql)
            query_sql = "select * from mission_table where id=%d;" % id
            try:
                cursor.execute(modify_sql)
                connection.commit()
                print("success modify")
                cursor.execute(query_sql)
                results = cursor.fetchall()
                for row in results:
                    id = row[0]
                    mission_name = row[1]
                    trigger_time = row[2]
                return (id, mission_name, trigger_time, True)
            except:
                connection.rollback();
                return (id, None, None, False)
    finally:
       db_disconn(connection);

def delete_mission(id):
    connection = db_conn()
    try:
        with connection.cursor() as cursor:
            del_sql = "delete from mission_table where id=%d;" % id
            logging.info("delete sql:" + del_sql)
            query_sql = "select * from mission_table where id=%d;" % id
            try:
                cursor.execute(query_sql)
                results = cursor.fetchall()
                for row in results:
                    id = row[0]
                    mission_name = row[1]
                    trigger_time = row[2]
                cursor.execute(del_sql)
                connection.commit()
                return (id, mission_name, trigger_time, True)
            except:
                connection.rollback();
                return (id, None, None, False)
    finally:
        db_disconn(connection);
        
def query_mission_by_id(id=0):
    connection = db_conn()
    try:
        with connection.cursor() as cursor:
            if id == 0:
                sql ="select * from mission_table;"
            else:
                sql = "select * from mission_table where id=%d;" % id;
            logging.info("sql query request: " + sql)
            cursor.execute(sql)
            results = cursor.fetchall()    
            for row in results:
                id = row[0]
                mission_name = row[1]
                trigger_time = row[2]
                # 打印结果
                print ("sql query result: id=%d,mission_name=%s,trigger_time=%s" % \
                        (id, mission_name, trigger_time ))
            return results
    finally:
        db_disconn(connection);
        
def query_mission_by_mission_name_and_trigger_time(mission_name="null", trigger_time="null"):
    connection = db_conn()
    try:
        with connection.cursor() as cursor:
            if mission_name=="null" and trigger_time=="null":
                sql ="select * from mission_table;"
            elif mission_name!="null":
                sql = "select * from mission_table where mission_name='%s';" % mission_name;
            elif trigger_time!="null":
                sql = "select * from mission_table where trigger_time='%s';" % trigger_time;
            else:
                sql = "select * from mission_table where mission_name='%s' and trigger_time='%s';" % (mission_name, trigger_time);
            logging.info("sql query request: " + sql)
            cursor.execute(sql)
            results = cursor.fetchall()    
            for row in results:
                id = row[0]
                mission_name = row[1]
                trigger_time = row[2]
                # 打印结果
                logging.info("sql query result: id=%d,mission_name=%s,trigger_time=%s" % \
                        (id, mission_name, trigger_time ))
            return results
    finally:
        db_disconn(connection);
        
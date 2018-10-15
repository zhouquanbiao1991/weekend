import pymysql



def add_mission(mission_name, trigger_time):
    connection = pymysql.connect(host="193.112.113.25",
                     user="weekend",
                     password="Z7URBdP7y8lPz7eU",
                     db="weekend" )
    try:
        with connection.cursor() as cursor:
            sql ="insert into mission_table (mission_name, trigger_time) values(%s, %s);"
            print("sql request: " + sql)
            try:
                cursor.execute(sql, (mission_name, trigger_time))
                connection.commit()
                return True
            except:
                print("database operation fail")
                connection.rollback();
                return False
    finally:
        connection.close();
        
def modify_mission(id, mission_name, trigger_time):
    #situtation have to be verify: no target mission
    connection = pymysql.connect(host="193.112.113.25",
                     user="weekend",
                     password="Z7URBdP7y8lPz7eU",
                     db="weekend" )
    try:
        with connection.cursor() as cursor:
            modify_sql = "update mission_table set mission_name='%s',trigger_time='%s' where id=%d" % (mission_name, trigger_time, id)
            print("modify_sql: " + modify_sql)
            query_sql = "select * from mission_table where id=%d;" % id
            print("query_sql: " + query_sql)
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
        connection.close();

def delete_mission(id):
    connection = pymysql.connect(host="193.112.113.25",
                     user="weekend",
                     password="Z7URBdP7y8lPz7eU",
                     db="weekend" )
    try:
        with connection.cursor() as cursor:
            del_sql = "delete from mission_table where id=%d;" % id
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
        connection.close();

def query_mission(id=-1):
    connection = pymysql.connect(host="193.112.113.25",
                     user="weekend",
                     password="Z7URBdP7y8lPz7eU",
                     db="weekend" )
    try:
        with connection.cursor() as cursor:
            if id == -1:
                sql ="select * from mission_table;"
                cursor.execute(sql)
            else:
                sql = "select * from mission_table where id=%d;" % id;
                print("sql query request: " + sql)
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
        connection.close();



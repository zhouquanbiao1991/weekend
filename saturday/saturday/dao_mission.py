import pymysql

connection = pymysql.connect(host="193.112.113.25",
                     user="weekend",
                     password="Z7URBdP7y8lPz7eU",
                     db="weekend" )

def add_mission(mission_name, trigger_time):
    try:
        with connection.cursor() as cursor:
            sql ="insert into mission_table (mission_name, trigger_time) values('%s', '%s');"
            try:
                cursor.execute(sql, (mission_name, trigger_time))
                connection.commit()
            except:
                connection.rollback();
    finally:
        connection.close();
        
def change_mission(id, mission_name, trigger_time):
    try:
        with connection.cursor() as cursor:
            sql = "update mission_table set mission_name='%s',trigger_time='%s' where id=%d"
            try:
                cursor.execute(sql, (mission_name, trigger_time, id))
                connection.commit()
            except:
                connection.rollback();
    finally:
        connection.close();

def delete_mission(id):
    try:
        with connection.cursor() as cursor:
            sql ="delete from title where id=%d;"
            try:
                cursor.execute(sql, id)
                connection.commit()
            except:
                connection.rollback();
    finally:
        connection.close();

def query_mission(id=-1):
    try:
        with connection.cursor() as cursor:
            if id == -1:
                sql ="select * from mission_table;"
                cursor.execute(sql)
            else:
                sql = "select id=%d from mission_table;"
                cursor.execute(sql, id)
            results = cursor.fetchall()    
            for row in results:
                id = row[0]
                mission_name = row[1]
                trigger_time = row[2]
                # 打印结果
                print ("id=%d,mission_name=%s,trigger_time=%s" % \
                        (id, mission_name, trigger_time ))
            return results
    finally:
        connection.close();




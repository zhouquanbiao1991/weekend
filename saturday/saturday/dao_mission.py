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
        
def change_mission(id, mission_name, trigger_time):
    connection = pymysql.connect(host="193.112.113.25",
                     user="weekend",
                     password="Z7URBdP7y8lPz7eU",
                     db="weekend" )
    try:
        with connection.cursor() as cursor:
            sql = "update mission_table set mission_name=%s,trigger_time=%s where id=%d"
            try:
                cursor.execute(sql, (mission_name, trigger_time, id))
                connection.commit()
            except:
                connection.rollback();
    finally:
        connection.close();

def delete_mission(id):
    connection = pymysql.connect(host="193.112.113.25",
                     user="weekend",
                     password="Z7URBdP7y8lPz7eU",
                     db="weekend" )
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




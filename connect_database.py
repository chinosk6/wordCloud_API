import pymysql
import settings


host = settings.mysql.host
port = settings.mysql.port
db = settings.mysql.db
user = settings.mysql.user
password = settings.mysql.password

def get_connection():
    conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password)
    return conn


def get_text(groupid:int, timestamp = 1624464000000): #2021-06-24 00:00:00

    #try:
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(("select Message,QQ from `%d` where (QQ != self) and (InsertTimestamp > %d)") % (groupid, timestamp)) 
    
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    if(len(data)<=0):
        return(False, "Message not found")

    return(True, data)

    #except OperationalError:
    #    return(False, "Access denied")

    #except Exception as err:
    #    return(False, repr(err))


#print(get_text("549090812")[1])

def change_table(): #修复bug用
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    list = []
    listr = open("C:\\Users\\Y7000\\Desktop\\1.txt", 'r', encoding='utf-8').readlines()
    for nb in listr:
        nb = nb.replace("\n", '')

    #try:
        cursor.execute(("ALTER TABLE `qqmsglog`.`%s` MODIFY COLUMN `QQ` bigint(20) NOT NULL FIRST, MODIFY COLUMN `GroupNum` bigint(20) NULL DEFAULT NULL AFTER `QQname`, MODIFY COLUMN `self` bigint(20) NULL DEFAULT NULL AFTER `InsertTime`;") % (nb)) 
    
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    if(len(data)<=0):
        return(False, "Message not found")

    return(True, data)
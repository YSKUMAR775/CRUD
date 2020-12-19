import pymysql


def db_connect3():
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='S@i30051995',
                         db='crud')
    return db

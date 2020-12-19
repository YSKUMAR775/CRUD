import pymysql


def db_connect3():
    db = pymysql.connect(host='aws2.c42ojr1a1cpj.ap-south-1.rds.amazonaws.com',
                         user='admin',
                         password='yskumar775',
                         db='crud')
    return db
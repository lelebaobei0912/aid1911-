import pymysql

#链接数据库
db = pymysql.connect(host='localhost',
                      port=3306,
                     user='root',
                     password='123456',
                     database= 'stu',
                     charset='utf8')
#生成游标对象 (操作数据库,执行sql语句,获取结果)
cur=db.cursor()
l = [('Lilei',17,'m',81),('Andy',18,'w',84),('Lili',19,'w',91)]
sql = "insert into cls (name,age,sex,score)" \
       " values (%s,%s,%s,%s);"
try:
    # for i in l:
    #     cur.execute(sql,i)
    cur.executemany(sql,l)
    db.commit()
except:
    db.rollback()

cur.close()
db.close()

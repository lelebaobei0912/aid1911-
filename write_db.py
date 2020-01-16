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


#执行写sql操作
# sql = "insert into cls (name,age,score)" \
#       " values (%s,%s,%s);"
# cur.execute(sql,['Tom',17,59])

sql = "update cls set sex='m' where name='Jame':"
cur.execute(sql)

# sql = "delete from cls where sex is null;"
# cur.execute(sql)

db.commit()#同步到数据库

#关闭游标和数据库链接
cur.close()
db.close()


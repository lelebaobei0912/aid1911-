""""
读数据库
"""
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


#执行读sql操作
sql = 'select name,age,score from cls;'
cur.execute(sql) # 执行sql 语句

#获取结果方法一
# for i in cur:
#     print(i)
#获取结果方法二
# one_row = cur.fetchone()  #获取一条记录
# print(one_row)

many_row = cur.fetchmany(3)#获取多条记录
print(many_row)

all_row = cur.fetchonall()# 获取所有记录
print(all_row)



#关闭游标和数据库链接
cur.close()
db.close()
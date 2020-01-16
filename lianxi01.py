import pymysql
db = pymysql.connect(host='localhost',
                      port=3306,
                     user='root',
                     password='123456',
                     database= 'stu',
                     charset='utf8')
cur=db.cursor()

name = input('输入一个学生姓名')

sql = 'select name,hobby,price ' \
      "from interest " \
      "where name='%s';"%name
cur.execute(sql)

print(cur.fetchall())


cur.close()
db.close()
""""
在dict数据库中建立words表存储单词
id word mean 三个字段
将dict.txt文件中所有单词存入这个数据表
注意后续操作为频繁的查询单词
"""
#创建words 数据表
# create table `words`(id int primary key auto_increment,word char(28) not null,mean varchar(1024),index(word));



import pymysql
import re
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')
cur = db.cursor()
f = open('dict.txt')
list = []
for line in f:
    #获取单词和解释
    # word,mean = line.split(' ',1)
    # print(word,"----",mean,strip())
    # 获取单词和解释
    tup = re.findall(r"(\w+)\s+(.*)",line)
    list.extend(tup) # 合并为一个列表
f.close()

sql="insert into words (word,mean) values (%s,%s);"
try:
    cur.executemany(sql,list)
    db.commit()
except:
    db.rollback()






# 关闭游标和数据库
cur.close()
db.close()


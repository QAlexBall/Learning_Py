'''
表是数据库中存放关系数据的集合, 一个数据库里面同常都包含多个表
要操作关系数据库, 首先需要连接到数据库, 一个数据库的连接称为Connection

连接到数据库后, 需要打开游标, 称之为Cursor, 通过Cursor执行SQL语句, 然后获得执行结果
Python定义了一套操作数据库的API接口, 任何数据库要连接到Python秩序提供Python标准的数据库驱动即可

由于SQLite的驱动内置在Python标准库中, 可以直接操作SQLite数据库
'''

'''
import sqlite3 # 导入SQLite驱动
conn = sqlite3.connect('test.db')# 连接到SQLite数据库
									# 数据库文件是test.db
										# 如果文件不存在, 会自动在当前目录创建
cursor = conn.cursor() # 创建一个Cursor
cursor.execute('create table user \ # 执行一条SQL语句, 创建user表:
	(id varchar(20) primary key,\
	 name varchar(20))')
cursor.execute('insert into user (id, name) values(\'1\', \'Alex\')')
print(cursor.rowcount) # 通过rowcount获得插入的行数
cursor.close() # 关闭Cursor
conn.commit() # 提交事务
conn.close() # 关闭Connection
'''
'''查询记录
conn = sqlite3.connect('test.db')
cursor = conn.cursor() # 执行查询语句
cursor.execute('select * from user where id=?', '1') # 获得查询结果集
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
'''
import os, sqlite3
'''
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
	os.remove(db_file)
	
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id var char(20) primary key, \
	name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()
'''
def get_score_in(low, high):
	# 返回指定分数区间的名字, 按分数从低到高排序
	pass
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user')
values = cursor.fetchall()
print(values[0])
cursor.close()
conn.close()
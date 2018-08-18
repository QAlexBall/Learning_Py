import mysql.connector # 导入MySQL驱动
conn = mysql.connector.connect(user='root', password='example', database='student')
# cursor = conn.cursor()
# # sql_1 = '''
# # create table test (
# # 	id varchar(20) primary key, 
# # 	name varchar(20))
# # 	'''
# # cursor.execute(sql_1)
# sql_2 = '''
# insert into test (id, name) values (%s, %s)
# 	'''
# cursor.execute(sql_2, ['1', 'Alex'])
# cursor.rowcount
# conn.commit()
# cursor.close()

cursor = conn.cursor()
sql_3 = '''
	select *
	from test
	where id = %s
	'''
cursor.execute(sql_3, ['1'])
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
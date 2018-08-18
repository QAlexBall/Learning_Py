# 数据库是一个二维表, 包含多行多列, 把一个表的内容用python
# 表示出来的话, 可以用一个list表示多行, list的每一个元素是tuple,
# 表示一行记录
# 但是用tuple表示一行很难看出表的结构, 如果把一个tuple用class实例来表示
# 就可以很容易的看出表的结构:
	# class User(object):
	# 	def __init__(self, id, name):
	# 		self.id = id
	# 		self.name = name
	# [
	# 	User('1', 'Alex'),
	# 	User('2', 'Bob'),
	# 	User('3', 'Adam')
	# ]
# 这就是ORM技术: Object-Relationnal Mapping, 把关系数据库的表结构映射到对象上.
# 由ORM框架来做这个转换, Python中有SQLAlchemy的ORM框架

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() # 创建对象的基类
class User(Base):
	__tablename__ = 'test' # 表名
	id = Column(String(20), primary_key=True) # 表的结构
	name = Column(String(20))
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/student') # 初始化数据库连接
DBSession = sessionmaker(bind=engine) # 创建DBSession类型

# 以上代码完成SQLAlchemy的初始化和具体每个表的class定义,
# 如果有多个表, 就继续定义其他class


session = DBSession() # 创建session对象
new_user = User(id='10', name='bob1') # 创建新的User对象
session.add(new_user) # 添加到session
session.commit() # 提交即保存到数据库
session.close() # 关闭数据库


session = DBSession()
user = session.query(User).filter(User.id=='5').one()
print('type:', type(user))
print('name:', user.name)
session.close()

# output: 
# type: <class '__main__.User'>
# name: bob
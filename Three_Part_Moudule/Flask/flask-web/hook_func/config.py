import os

# session config
SECRET_KEY = os.urandom(24)

# db config
USERNAME = 'root'
PASSWORD = 'zhuderen'
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'hook_func'

# mysql+mysqldb://root:zhuderen@127.0.0.1:3306/hook_func
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(
    USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
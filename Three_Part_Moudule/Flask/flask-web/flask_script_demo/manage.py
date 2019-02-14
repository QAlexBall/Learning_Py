# encoding: utf-8

from flask_script import Manager
from db_scripts import db_manager
from app import app

manager = Manager(app)

# 和数据库相关的操作

@manager.command
def runserver():
    print('run server')

manager.add_command('db', db_manager)

if __name__ == '__main__':
    manager.run()
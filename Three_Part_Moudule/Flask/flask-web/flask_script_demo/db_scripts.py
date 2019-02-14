# encoding: utf-8

from flask_script import Manager

db_manager = Manager()

@db_manager.command
def init():
    print('db init!')

@db_manager.command
def migrate():
    print('db table migrate!')
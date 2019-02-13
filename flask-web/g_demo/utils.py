from flask import g

def login_log():
    print('username: ', g.username)

def login_id_log(id):
    pass
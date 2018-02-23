# python的hashlib提供了常见的摘要算法, 如MD5, SHA1等等
# 摘要算法称为哈希算法, 散列算法, 它通过一个函数, 把任意长的数据
# 转化成一个长度固定的数据串(通常用16进制的字符串表示)
# 摘要函数是一个单项函数, 计算f(data)很容易, 但通过digest反推data却非常困难

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
print(md5)
print(md5.__sizeof__())

md51 = hashlib.md5()
md51.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md51.hexdigest())

md51 = hashlib.md5()
md51.update('how to use md5 in'.encode('utf-8'))
md51.update('python hashlib?'.encode('utf-8'))
print(md51.hexdigest())
print(dir(md51))

# MD5是最常见的摘要算法, 速度很快, 生成结果是固定的128bit字节, 通常用一个32位的16进制字符串表示
# 另一种常见的摘要算法是SHA1, 调用SHA1和MD5完全类似
import hashlib
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in'.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest()) # SHA1的结果是160字节的, 通常用一个40位的16进制字符串表示

# 摘要算法应用
# 正确的保存口令的方式不是存储用户的明文口令
# 而是存储用户口令的摘要, 防止数据库泄露而导致的口令泄露

# 先计算出常用口令的MD5值, 得到反推表, 对比数据库的MD5, 获取口令


# 加盐
# 通过添加一个复杂字符串
def calc_md5(password):
	return get_md5(password + 'the-Salt')
# 只要Salt不被黑客知道就很难通过MD5反推明文口令


# 根据用户输入的用户名和口令模拟用户注册, 计算更安全的MD5
db = {'bob', 12345}
username = 0

def get_md5(passwd):
	return 
def register(username, password):
	db[username] = get_md5(password + username + 'the-Salt')


# 根据修改后的MD5算法实现用户登陆的验证
def login(username, password):
	pass

import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()
class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}
def login(username, password):
    user = db[username]
    return user.password == get_md5(password)
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
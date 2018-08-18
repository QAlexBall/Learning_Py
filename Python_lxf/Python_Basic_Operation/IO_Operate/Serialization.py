# 把从内存中变成可存储或传输的过程称之为序列化
# Python中叫做pickling, 反序列化即unpickling
# Python中提供了pickle模块来实现序列化
import pickle
'''
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

f = open('File/dump.txt', 'wb')
pickle.dump(d, f)
f.close()
'''
with open('File/dump.txt', 'rb') as f:
	d = pickle.load(f)
print(d)

# JSON
# 如果需要在不同变成语言之间传递对象, 就必须把对象序列化成标准格式
# JSON表示出来就是一个字符串, 可以被所有语言读取, 也可以方便地存储到
# 磁盘上或在网络上传输, JSON可以直接在Web页面中读取
import json
d = dict(name='Bob', age=20, score=88)
dumps_d = json.dumps(d)
print(dumps_d)
loads_d = json.loads(dumps_d)
print(loads_d)

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score
def studnent2dict(std):
	return {
	'name' : std.name,
	'age' : std.age,
	'score' : std.score
	}
s = Student('Bob', 20, 88)
# print(json.dumps(s)) TypeError: Object of type 'Student' is not JSON serializable
json_dumps_s = json.dumps(s, default=studnent2dict)
json_dumps_s1 = json.dumps(s, default=lambda obj: obj.__dict__)
print(json_dumps_s, json_dumps_s1)
def dict2student(d):
	return Student(d['name'], d['age'], d['score'])
json_loads_s = json.loads(json_dumps_s, object_hook=dict2student)
print(json_loads_s, json_loads_s.name)

# with open('File/json_dumps.txt', 'wb') as f: not a byte it's str
with open('File/json_dumps.txt', 'w') as f:
	json.dump(s, f, default=studnent2dict)
with open('File/json_dumps.txt', 'r') as f:
	json_load_s = json.load(f)
print(json_load_s)
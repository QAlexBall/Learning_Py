"""
list是一种有序的集合,可以随时添加和删除其中的元素
"""
classmates = ['machael', 'bob', 'tracy']
print(classmates, len(classmates), classmates[0], classmates[-1])

classmates.append('adam')
classmates.insert(1, 'jack')
print(classmates)

classmates.pop()
classmates.pop(1)
classmates[1] = 'sarah'
print(classmates)

L = ['apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(L)
print(s, len(s))

"""
另一种有序表叫元组: tuple, tuple一旦初始化就不能修改
"""
classmates = ('michael', 'bob', 'tracy')
t = (1, 2)
w = (1, 3, 5, [1, 3])
# t[0] = 2 error
w[3][0] = 3 # tuple 中的list可以被修改
print(t)
print(w)

for name in classmates:
	print('hello %s' % name)
	

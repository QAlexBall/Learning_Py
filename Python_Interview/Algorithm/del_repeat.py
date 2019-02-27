'''
去除列表中的重复元素
'''

l = list((1, 2, 3, 3, 7, 5, 6, 5))
print(l)

# solution 1
del_l = list(set(l))
print(del_l)

# solution 2
l2 = []
[l2. append(i) for i in l if not i in l2]
print(l2)


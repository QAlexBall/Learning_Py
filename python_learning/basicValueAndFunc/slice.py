L = ['michael', 'sarah', 'tracy', 'bob', 'jack']
# 取前N个元素
r = []
n = 3
for i in range(n):
	r.append(L[i])
print(r)
# python提供slice操作符简化.
m = 0
print(L[m:n], L[:n], L[-n:-1])


L = list(range(100))
print(L[:10], '\r', L[-10:], '\r', L[10:20], '\r', L[:10:2], '\r', L[::5])
print((0, 1, 2, 3, 4, 5)[:3])
print('ABCDEFG'[:3], 'ABCDEFG'[::2])





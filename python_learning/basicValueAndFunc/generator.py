L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print(L, '\n', g, next(g), next(g), next(g))
# 费波拉契数列
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b, ' ', end='')
		a, b = b, a + b
		n = n + 1
	return 'done'
print(fib(6))

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'
f = fib(6)
print(next(f), next(f), next(f))
g = fib(6)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value: ', e.value)
		break

def odd():
	print(' step 1')
	yield 1
	print(' step 2')
	yield 2
	print(' step 3')
	yield 3
o = odd()
print(next(o), next(o))

"""
杨辉三角形
""" 
def triangles():
	N = [1]
	while True:
		yield N
		N.append(0)
		N = [N[i]+N[i-1] for i in range(len(N))]

f = triangles()
print(next(f), next(f), next(f), next(f), next(f))
if __name__ == "__main__":
	n = 0
	for t in triangles():
		print(t)
		n = n + 1
		if n == 10:
			break
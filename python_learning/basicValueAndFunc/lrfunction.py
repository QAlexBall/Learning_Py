import math

def quadratic(a, b, c):
	x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
	x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
	return x1, x2

result = quadratic(1, -4, 3)
print(result)

def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)
print(fact(5))

L = []
n = 1
while n <= 20:
	L.append(n)
	n = n + 2
print(L)


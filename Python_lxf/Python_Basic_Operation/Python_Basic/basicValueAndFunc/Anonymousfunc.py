l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
def f(x):
	return x * x
print(f, f(3))

f = lambda x: x * x
print(f, f(5))
def build(x, y): 
	# return x * x + y * y
	return lambda: x * x + y * y
a = build(3, 7)
print()
print(a(), '  ', l)

a = lambda x, y: x * x + y * y
print(a(3, 7))


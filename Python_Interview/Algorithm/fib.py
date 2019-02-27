'''
1.台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

# solution1
fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
print(fib(3))

# solution2
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def fib(i):
    if i < 2:
        return 1
    return fib(i - 1) + fib(i - 2)
print(fib(4))

# solution3
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b
print(fib(3))

'''
2. 变态台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
fib = lambda n : n if n < 2 else 2 * fib(n - 1)
print(fib(3))

'''
3. 矩形覆盖
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''

f = lambda n : 1 if n < 2 else f(n - 1) + f(n - 2)
print(f(4))


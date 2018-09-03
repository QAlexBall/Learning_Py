### \*args 和 \*\*kwargs

* \*args = 参数列表-作为可选参数
* *\*kwargs = 字典-参数的关键字作为键,它们的值作为字典的值.

***

```python
def foo(*args, **kwargs):
    print('args = ', args)
    print('kwargs = ', kwargs)
    print('-----------------')
 
if __name__ == '__main___':
    foo(1, 2, 3, 4)
    foo(a=1, b=2, c=3)
    foo(1, 2, 3, 4, a=1, b=2, c=3)
    foo('a', 1, None, a=1, b='2', c=3)
'''
output:
args =  (1, 2, 3, 4)
kwargs =  {}
-----------------
args =  ()
kwargs =  {'a': 1, 'b': 2, 'c': 3}
-----------------
args =  (1, 2, 3, 4)
kwargs =  {'a': 1, 'b': 2, 'c': 3}
-----------------
args =  ('a', 1, None)
kwargs =  {'a': 1, 'b': '2', 'c': 3}
'''
```

#####  \*args的用法

* \*args和\*\*kwargs主要用于函数定义.可以将**不定数量的参数**传递给一个函数.
* 这里**不定**的意思是: 预先并不知道,函数使用这会传递多少个参数,所以在这个场景下使用这两个关键字.
* \*args是用来发送一个非键值对的可变数量的参数列表给一个函数.

```python
def test_var_args(f_arg, *argv):
    print("first normal arg: ", arg)
    for arg in argv:
        print("another arg through *argv: ", arg)
        
test_var_args('yasoob', 'python', 'eggs', 'test')
```

##### \*\*kwargs的用法

* \*\*kwargs允许将不定长的键值对,作为参数传递给一个函数

```python
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))
        
        
>>> greet_me(name="hello")
name == hello
```



***

### Python zip()函数

**zip()函数用于将可迭代的对象作为参数,将对象中对应的元素打包成一个个元组,然后返回这些元组组成的列表**

**(python3中,zip()返回的是一个对象,如需展示列表,需要手动list()转换)**

如果各个迭代器的元素个数不一致,则返回列表长度与最短的对象相同,利用\*号操作符,可以将元组解压为列表.

```shell
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = [4, 5, 6, 7, 8]
>>> zipped = zip(a, b)  # 返回一个对象
>>> zipped
<zip object at 0x7faaca989588>
>>> list(zipped)        # list()转换为列表
[(1, 4), (2, 5), (3, 6)]
>>> a1, a2 = zip(*zip(a, b))    # 与zip相反,*zip可理解为解压,返回二位矩阵
>>> list(a1)
[1, 2, 3]
>>> list(a2)
[4, 5, 6]
>>> a1
>>> (1, 2, 3)
```



### Reduce

* 当需要对一个列表进行一些计算并返回结果时,可以使用Reduce
* reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

```python
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)
# Output: 24
```


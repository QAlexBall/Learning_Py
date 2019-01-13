### 用户定义的可调用类型
不仅Python函数是真正的对象,任何Python对象都可以表现得像函数.为此,只需要实现实例方法__call__.

### 函数内省
使用dir()函数可探知func所有具有的属性.
与用户定义的常规类一样,函数使用__dict__属性存储赋予它的用户属性.
列出常规对象没有而函数有的属性:
```bash
>>> class C: pass
...
>>> obj = C()
>>> def func(): pass
...
>>> sorted(set(dir(func)) - set(dir(obj)))
['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
```
### 函数注解
Python3提供了一种句法,用于为函数声明中的参数和返回值附加元数据.
```python
# 有注解的clip函数
from inspect import signature

def clip(text:str, max_len:'int > 0'=80) -> str:
    """在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None: # 没有找到空格
        end = len(text)
    return text[:end].rstirp()

print(clip.__annotations__) # {'text': <class 'str'>, 'max_len': 'int > 0', 'return': <class 'str'>}
sig = signature(clip)
print(sig.return_annotation)
for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13)
    print(note, ':', param.name, '=', param.default)
# <class 'str'> : text = <class 'inspect._empty'>
# 'int > 0'     : max_len = 80
```

### tips
1. 调用类时会运行类的__new__方法创建一个实例,然后运行__init__方法,初始化实例,最后把实例返回给调用方.因为Python没有new运算符,所以调用类相当与调用函数.
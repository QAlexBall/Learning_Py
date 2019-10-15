"""
inspect模块提供了一些游泳的函数帮助获取对象的信息，例如模块，类，方法，函数，回溯，帧对象以及代码对象。
该模块主要提供了4中功能：类型检查，获取源代码，检查类与函数，检查解释器的调用堆栈
"""

import inspect
from inspect import signature


def spam(x, y, z=42):
    pass


sig = signature(spam)
print(sig)
print(sig.parameters)
print(sig.parameters['z'].name)
print(sig.parameters['z'].default)
print(sig.parameters['x'].default)
print(sig.parameters['z'].kind)

# sig = (x, y, z=42)
# sig.parameters = OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">), ('z', <Parameter "z=42">)])
# sig.parameters['z'].name = z
# sig.parameters['z'].default = 42
# sig.parameters['x'].default = <class 'inspect._empty'>
# sig.parameters['z'].name = POSITIONAL_OR_KEYWORD

bound_types = sig.bind_partial(int, z=int)
print(bound_types)  # <BoundArguments (x=<class 'int'>, z=<class 'int'>)>

bound_values = sig.bind(1, 2, 3)
print(bound_values.arguments)  # OrderedDict([('x', 1), ('y', 2), ('z', 3)])

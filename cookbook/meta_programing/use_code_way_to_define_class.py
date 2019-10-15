# def __init__(self, name, shares, price):
#     self.name = name
#     self.shares = shares
#     self.price = price
#
#
# def __str__(self):
#     return "<Class Stock (name, {}))>".format(self.name)
#
#
# def cost(self):
#     return self.shares * self.price
#
#
# cls_dict = {
#     '__init__': __init__,
#     '__str__': __str__,
#     'cost': cost
# }
#
# import types
#
# Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
# Stock.__module__ = __name__
#
# s = Stock('ACME', 50, 91.1)
# print(s)
#
# import abc
#
#
# class Spam(abc, debug=True, typecheck=False):
#     pass
#
#
# Spam1 = types.new_class('Spam1',
#                         (abc,),
#                         {'debug': True, 'typecheck': False},
#                         lambda ns: ns.update(cls_dict))

import operator
import sys
import types


def named_tuple(classname, fieldnames):
    cls_dict = {name: property(operator.itemgetter(n)) \
                for n, name in enumerate(fieldnames)}

    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))
        return tuple.__new__(cls, args)

    cls_dict['__new__'] = __new__

    cls = types.new_class(classname, (tuple,), {},
                          lambda ns: ns.update(cls_dict))
    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls

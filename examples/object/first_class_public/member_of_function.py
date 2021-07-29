def operator_1(x):
    return x + 1

def operator_2(x):
    return x + 2

def __add__(self, other):
    import pdb; pdb.set_trace()

operator_1.__add__ = __add__
operator_1.__radd__ = __add__
operator_1.__iadd__ = __add__
operator_1.__iconcat__ = __add__
operator_2.__add__ = __add__
operator_2.__radd__ = __add__
operator_2.__iadd__ = __add__
operator_2.__iconcat__ = __add__

import types

import pdb

types.FunctionType.__add__ = lambda x, y: pdb.set_trace()
import pdb; pdb.set_trace()

print((operator_1 + operator_2)(0))

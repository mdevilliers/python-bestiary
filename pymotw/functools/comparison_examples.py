# https://pymotw.com/2/functools/
import functools
import inspect
from pprint import pprint

@functools.total_ordering
class MyObject(object):
    def __init__(self, val):
        self.val = val

    # The class must provide an implmentation of __eq__() 
    # and any one of the other rich comparison methods. 
    # The decorator adds implementations of the other 
    # methods that work by using the comparisons provided.
    def __eq__(self, other):
        print '  testing __eq__(%s, %s)' % (self.val, other.val)
        return self.val == other.val
    def __gt__(self, other):
        print '  testing __gt__(%s, %s)' % (self.val, other.val)
        return self.val > other.val

print 'Methods:\n'
pprint(inspect.getmembers(MyObject, inspect.ismethod))

a = MyObject(1)
b = MyObject(2)

print '\nComparisons:'
for expr in [ 'a < b', 'a <= b', 'a == b', 'a >= b', 'a > b' ]:
    print '\n%-6s:' % expr
    result = eval(expr)
    print '  result of %s: %s' % (expr, result)
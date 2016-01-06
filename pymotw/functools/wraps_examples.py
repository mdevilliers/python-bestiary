# https://pymotw.com/2/functools/
import functools

def show_details(name, f):
    """Show details of a callable object."""
    print '%s:' % name
    print '\tobject:', f
    print '\t__name__:', 
    try:
        print f.__name__
    except AttributeError:
        print '(no __name__)'
    print '\t__doc__', repr(f.__doc__)
    print
    return

def simple_decorator(f):
    @functools.wraps(f)
    def decorated(a='decorated defaults', b=1):
        print '\tdecorated:', (a, b)
        print '\t',
        f(a, b=b)
        return
    return decorated

def myfunc(a, b=2):
    print '\tmyfunc:', (a,b)
    return
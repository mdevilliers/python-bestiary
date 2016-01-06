# https://pymotw.com/2/functools/
import functools

def myfunc(a, b=2):
    """Docstring for myfunc()."""
    print '\tcalled myfunc with:', (a, b)
    return

def show_details(name, f, is_partial=False):
    """Show details of a callable object."""
    print '%s:' % name
    print '\tobject:', f
    if not is_partial:
        print '\t__name__:', f.__name__
    print '\t__doc__', repr(f.__doc__)
    if is_partial:
        print '\tfunc:', f.func
        print '\targs:', f.args
        print '\tkeywords:', f.keywords
    return

class MyClass(object):
    """Demonstration class for functools"""
    
    def meth1(self, a, b=2):
        """Docstring for meth1()."""
        print '\tcalled meth1 with:', (self, a, b)
        return
    
    def meth2(self, c, d=5):
        """Docstring for meth2"""
        print '\tcalled meth2 with:', (self, c, d)
        return
    wrapped_meth2 = functools.partial(meth2, 'wrapped c')
    functools.update_wrapper(wrapped_meth2, meth2)
    
    def __call__(self, e, f=6):
        """Docstring for MyClass.__call__"""
        print '\tcalled object with:', (self, e, f)
        return

def show_class_details(name, f):
    """Show details of a callable object."""
    print '%s:' % name
    print '\tobject:', f
    print '\t__name__:', 
    try:
        print f.__name__
    except AttributeError:
        print '(no __name__)'
    print '\t__doc__', repr(f.__doc__)
    return

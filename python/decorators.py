"""
This script is for playing around with decorators.

It also shows the use of @classmethod and @staticmethod decorators
"""

def dec(func):
    def wrapper(*args, **kwargs):
        print "I'm doing something before the function"
        func(*args, **kwargs)
        print "I'm doing something after the function"

    return wrapper

@dec
def some_function(x):
    print "Whee!"
    print "Given x =",x


class myclass(object):
    def __init__(self):
        self.attr1 = 1
        self.attr2 = 2
        self.attr3 = 3

    @classmethod
    def class_method(cls, x):
        print "Executing class_method(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        print "Executing static_foo(%s)"%x

A = myclass()

A.class_method(1)

A.static_foo(1)


print A.class_method

print A.static_foo

print "What about calling myclass.static_foo from 'outside' the class?"
print myclass.static_foo(3)

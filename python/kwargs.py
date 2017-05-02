"""
module for playing around with keyword arguments and a class
with default values
"""

def printd(d):
    for key,val in d.iteritems():
        print key, val


class kw(object):
    _defaults = {'a':0, 'b':1}
    _keyerr = "Unexpected keyword argument '{0}' passed"

    def __init__(self,**kwargs):
        self.rc = kw._defaults.copy()
        print "Defaults"
        printd(self.rc)

        for (key,value) in kwargs.iteritems():
            if key not in self.rc:
                raise KeyError(kw._keyerr.format(key))
            else:
                self.rc[key]=value

        print "Updated Defaults"
        printd(self.rc)

no_kw = kw()

update_kw = kw(a=4, b=12)

# new_kw = kw(c=31)

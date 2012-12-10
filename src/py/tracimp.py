# try to recursively hook imports

import inspect
import __builtin__
savimp = __builtin__.__import__

def newimp(name, *x):
  caller = inspect.currentframe().f_back
  print "importing %s" % (name,)
  print list(caller.f_globals.items()), caller.f_globals.get('__name__')
  inspect.currentframe().f_globals['__builtins__'].__import__ = newimp
  return savimp(name, *x)

__builtin__.__import__ = newimp

import ast

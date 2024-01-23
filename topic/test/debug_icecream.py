from icecream import ic
'''
ic() is like print(), but better:

#https://github.com/gruns/icecream

To run demo: `python topic/test/debug_icecream.py`
'''


# Demo 1
def foo(i):
  return i + 333


ic(foo(123))
# ic| foo(123): 456

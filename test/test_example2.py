import pytest
from topic.test.unittest_func import add_numbers

'''
ImportError while importing test module '/data/data/com.termux/files/home/projects/sb-python-playround/topic/test/test_example2.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
../../../usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
topic/test/test_example2.py:2: in <module>
    from topic.test.unittest_func import add_numbers
E   ModuleNotFoundError: No module named 'topic'
=============================================== short test summary info ================================================
ERROR topic/test/test_example2.py


Fixed after add
/test/__init_.py
/topic/__init_.py

'''
'''
def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, -1) == -2

'''    
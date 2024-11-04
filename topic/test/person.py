# Geneate by ChatGPT

'''
ImportError while importing test module '/data/data/com.termux/files/home/projects/sb-python-playround/test/test_person.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
../../../usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
test/test_person.py:2: in <module>
    from topic.test.person import Person
E   ModuleNotFoundError: No module named 'topic'
'''
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def is_adult(self):
        return self.age >= 18
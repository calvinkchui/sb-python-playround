class Class:
    def foo():
        pass

c = Class()
print (c.foo.__name__) # foo - function name
print (c.foo.__qualname__) #Class.foo - Class + name


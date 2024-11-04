#https://mark1002.github.io/2018/07/31/python-%E5%AF%A6%E7%8F%BE-singleton-%E6%A8%A1%E5%BC%8F/

class SingleTonNew: 
    _instance = None 
    def __new__(cls, *args, **kwargs): 
        print ("SingleTonNew.__new__")
        if cls._instance is None: 
            print ("SingleTonNew.__new__ ( _instance is None)")
            cls._instance = super().__new__(cls) 
            
        return cls._instance 
         
    def __init__(self, a, b): 
        self.a = a 
        self.b = b
        print ("SingleTonNew.__init__")

s1 = SingleTonNew(a=11, b=21)
s2 = SingleTonNew(a=11, b=21)

print( id(s1) )
print( id(s2) )

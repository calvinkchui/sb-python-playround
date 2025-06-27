
def testfx(a):
    return "testfx[" + a + "]"

class Test:
    def __init__(self, name):
        self.name = name

    def testfx(self):
        return "Test.testfx[" + self.name + "]"

    def testfxParm(self, a):
        return "Test.testfxParm[" + self.name + "," + a + "]"
    
def demo01():
    print("eval (basic) ")
    a = 100
    t = Test("TestObj")
    print( eval("a") )
    print( "t.name=", eval("t.name") )
    print( "t.testfx=", eval("t.testfx()") )
    print( "t.testfxParm(x)=", eval("t.testfxParm('x')") )
    print( eval("testfx('func call')") )


def demo():
    demo01()    
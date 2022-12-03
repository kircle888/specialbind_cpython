# global
x = 2
y = 2
z = 2
def test_funcdef():
    x = 1
    y = 1
    z = 1
    print("FuncDef Test Start")
    def inner1():
        print("Inner1")
        print(x)# 1
        print(y)# 1
        print(z)# 1
    
    def inner2()[+x, y]: # + 表示许可且仅许可后续变量再束定 
        print("Inner2")
        print(x)# 1
        print(y)# 1
        print(z)# 2
    
    def inner3()[-x]: # - 表示限制且仅限制后续变量再束定 
        print("Inner3")
        print(x)# 2
        print(y)# 1
        print(z)# 1
    
    def inner4()[+]:
        print("Inner4")
        print(x)# 2
        print(y)# 2
        print(z)# 2
    
    inner1()
    inner2()
    inner3()
    inner4()
    print("FuncDef Test End")

def test_lambda():
    x = 1
    y = 1
    z = 1
    print("Lambda Test Start")
    inner1 = lambda : (x<<16)+(y<<8)+z
    inner2 = lambda [+x, y] : (x<<16)+(y<<8)+z
    inner3 = lambda [-x] : (x<<16)+(y<<8)+z
    inner4 = lambda [+] : (x<<16)+(y<<8)+z
    
    i1 = inner1()
    print("Inner1",(i1>>16)&0xff,(i1>>8)&0xff,(i1)&0xff)
    i2 = inner2()
    print("Inner2",(i2>>16)&0xff,(i2>>8)&0xff,(i2)&0xff)
    i3 = inner3()
    print("Inner3",(i3>>16)&0xff,(i3>>8)&0xff,(i3)&0xff)
    i4 = inner4()
    print("Inner4",(i4>>16)&0xff,(i4>>8)&0xff,(i4)&0xff)
    print("Lambda Test End")

if __name__ == "__main__":
    test_funcdef()
    test_lambda()


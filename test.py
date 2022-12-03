# global
x = 2
y = 2
z = 2
def outer():
    x = 1
    y = 1
    z = 1
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
    
    inner1()
    inner2()
    inner3()

if __name__ == "__main__":
    outer()


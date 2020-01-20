#Python Module : mod1

#To make a pyhon module
if(__name__ == '__main__'):
        print('The name of the mod1 is',__name__)
        print('The package of the mod1 is',__package__)
        print('----------------------------mod1 start -------------------------------')
        pass

print('The name of the mod1 is',__name__)
print('The package of the mod1 is',__package__)
def add(num1,num2):
    return num1+num2
    pass

def sub(num1,num2):
    return num1-num2
    pass

mulFunc =lambda num1,num2:num1*num2

PI = 3.14159 #원주율

class ModClass:
    staticField = 10
    confirm = 40 #변수명이 겹칠때는 instance field값이 없다
    def __init__(self):
        print("Mod1Class __init__ invoked")
        super().__init__()
        self.instanceField = 20
        self.confirm = 30
        pass

    def method1(self):
        print("Mod1Class method1 invoked")
        return "method1 호출 성공"
    pass

if(__name__ == '__main__'):
        print('----------------------------mod1 end -------------------------------')
        pass

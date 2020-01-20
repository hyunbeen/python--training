#sample2.py
#User-defined type(사용자 정의 타입)
#객체를 통해서, 생성한 속성(필드)을 
#OOP에서는 '인스턴스 필드(객체변수)'라고 부른다
#dir()
#del()
#globals()
#파이썬 언어에서는 모든게 객체인데 객체의 최상위(가장 높은 조상)클래스
#이름 -- object


# class Calculator:
#     pass

# calc1 = Calculator()
# calc2 = Calculator()

# print(type(calc1))
# print(id(calc1))
# print(calc1)

# print(type(calc2))
# print(id(calc2))
# print(calc1)
import random as rd
class Calculator:
    #Constructor
    #객체의 속성을 초기화(만들어낸다) 수행
    def __init__(self,color=None,shape='round',material=None):
        print('Calculator __init__ invoked')
        print('self : ',self)
        #색상속성(==색상필드)
        self.color = color
        self.shape = shape
        self.material = material

        pass
    #메소드 만들기
    def wriggle(self):
        print("%s 색깔의 전자계산기가 꿈틀거리다"%(self.color))
        self.wriggle2(3)
        self.weight = 50
        pass

    def wriggle2(self,value):
        print(value)
        print("%s 색깔의 전자계산기가 꿈틀거리다2"%(self.color))
       
        pass
    
    
    pass



    
print(rd.__name__)
print(__name__)
# calc1 = Calculator(material="plastic",color="red",shape="round")
# calc1 = Calculator('red')
calc1 = Calculator()
print(calc1.color)
# print(calc1.shape)#순서대로 값이들어가고 나머지는 default값이 들어간다
# calc2 = Calculator()
# print(calc2)
#__name__ : 현재 실행되고 있는 파이썬 모듈의 이름
#import module을 제외한 실행되고있는 파일은 __main__

# calc1.wriggle()
# print(calc1.weight) #다른 함수에서 속성 만드는거 가능
# calc1.price = 500
# print(calc1.price) #class 밖에서 속성 만드는거 가능

# a = FourCal()
# a.setdata(4, 2)
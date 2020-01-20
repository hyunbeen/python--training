#sample4.py
#클래스간의 관계
#사용,집합,상속
#사용(일회성),집합(속성의 하나로),상속(기능을 물려받는 것)
#자식이 부모를 상속받으면 자동으로 init안에 super를 호출한다
#
class Screen:
    # 속성의 종류
    # 1)객체의 고유한 속성
    # 2)집합관계있는 부품
    # 3)시간에 따라 값이 변하는 상태
    pass

class FourCal :
    
    def __init__(self):
        print('-Parent::__init__invoked')
        self.newnumber = 0
        self.result = 0
        self.screen = Screen()
        super().__init__()
        pass
    
  
    def add(self,newnumber):
        self.result += newnumber
        return(self.result)
        pass
    
    def sub(self,newnumber):
        self.result -= newnumber
        return(self.result)
        pass

    def mul(self,newnumber):
        self.result *= newnumber
        return(self.result)
        pass

    def div(self,newnumber):
        self.result /= newnumber
        return(self.result)
        pass

    pass

class MoreCal(FourCal):#자식 클래스

    def __init__(self):
        print('-Child::__init__invoked')
        # super().__init__() 

        # print(type(super))
        # print(dir(super))
        # print(type(super()))
        # print(dir(super()))

        # parent = super()
        # parent.__init__()


    def pow(self,newnumber):

        self.result **= newnumber
        return(self.result)
        pass
    def setresult(self,num):
        self.result = num       
        pass
    pass


# import pprint as pp
# pp.pprint(dir(calc))
# pp.pprint(globals())

calc = MoreCal()

print(type(calc))
print(id(calc))
print(calc)
calc.setresult(3)
print(calc.pow(4))

print(calc.add(4))




class Screen:
    # 속성의 종류
    # 1)객체의 고유한 속성
    # 2)집합관계있는 부품
    # 3)시간에 따라 값이 변하는 상태
    pass

class Fourcal :
    
    def __init__(self):
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

Calc = Fourcal()
print(Calc.add(3)) #0+3=3
print(Calc.sub(4)) #3-4=-1
print(Calc.mul(5)) #-1*5=-5
print(Calc.div(6)) #-5/6=-0/833333....
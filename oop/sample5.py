class FourCal :
    #클래수변수(x)-->정적필드(static field)
    #어느 특정 객체마다 고유하게 값을 가지고있는
    #필드가 아니라, 이클래스로부터 생성된
    #모든 객체에 공통적으로 사용가능한 공유필드
    lastname = "김"
    def __init__(self):
        print('-Parent::__init__invoked')
        #이 클래스에서 생성된 객체의 인스턴스필드(=객체변수)
        self.newnumber = 0
        self.result = 0
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

class SafeFourCal(FourCal):
    def __init__(self):
        print("SafeFourCal __init__ invoked")
        # super().__init__()
    #Method Overloading
    #같은 이름의 메소드를 여러개 정의 가능
    #Method Overriding
    def div(self,newnumber):
        if(newnumber == 0):
            return 0
        
        self.result /= newnumber
        return self.result

        pass

    
    pass

a = SafeFourCal()
print(a.lastname)
# print(a.div(0))
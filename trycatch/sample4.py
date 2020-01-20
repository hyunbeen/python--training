# 다형성 : 부모클래스가 물려준 메소드를,자식클래스가 재정의 하였을때
#          자식클래스로부터 생성된 자식객체가 해당 메소드를 호출 했을때,
#          부모가 물려준 메소드를 호출하지않고, 자식이 재정의(Overriding)
#          한 메소드가 호출됨으로써 다양한 기능을 수행할수 있게 되었다
#          (Polymorphism)

class Bird:
    def fly(self):
        raise MyError()

class Eagle(Bird):
    def fly(self):
        print("very fast")
    pass

class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)


# say_nick("천사")
# say_nick("바보")

eagle = Eagle()
eagle.fly()

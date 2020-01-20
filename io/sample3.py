#io/sample3.py

def add(num1,num2):
    print('- add(%d,%d) invorked'%(num1,num2))
    return num1+num2
    pass

# result = add(num1=1,num2=2)
result = add(num2=2,num1=1)#이름이 정해져 있기 때문에 순서가 바뀌어도 상관없다
print(result)

# def printvalue(*vlaue) 0개이상의 다양한 인자의 개수를 받을 수 있다
# 몇개이든 어떤 인자든 받아들일수 있는 함수를 가변인자(Variant argument)(0~ㅜ개의 전달인자 값이 전달가능)
# 블록안에는 튜플인자로 받아들여 진다

#1)함수선언시 매개변수리스트를 구성할때, 일반적인 형태의 매개변수 --> Positional Argument
#2)*붙은 Variant Argument(가변인자 매게변수) --> Variant Argument --> tuple type
#3)**붙은 Keyword Argument -->dict type
#변수를 섞어서 사용시에 positional argument가 제일 앞에서 나와야한다
#1)->2)->3) 순서로 사용하여야 한다

def printvalue(*value):
    print('- printvalue({0}) invorked'.format(value))
    print(type(value))
    print(value)
    print("-"*60)
    for i in value:
        print(type(i))

        if(type(i) is int):
            print("정수출력")
        if(type(i) is tuple):
            print("튜플출력")
        if(type(i) is set):
            print("set출력")
        if(type(i) is list):
            print("list출력")
        
        print(i)
    print("-"*60)
    pass

def printvalue2(**value):
    print('- printvalue2({0}) invorked'.format(value))
    print(type(value))
    print(value)
    pass

print("-"*60)

printvalue()
printvalue(1,2)
printvalue({1,2,3},[1,2])

printvalue2()
printvalue2(a=1)
printvalue2(name='foo',age=3) #dict로 들어가서 키 값은 문자열로 바뀐다
                              #이름 규칙 :영어 대소문자와 아리비아 숫자 가능하고 섞어서 가능하지만 아라비아 숫자로 시작하면 안된다

dictionary = {(1,2,3):"123"}
print(dictionary)
# printvalue2({'a':1})
tuple1 = [1,2,3]
# printvalue2(tuple1="123") 오류
printvalue2(tuple1="123")#안된다

print("-"*60)

#섞어서 변수를 쓸경우에
def func1(pos1,pos2):
    pass

def func2(pos1,pos2,*vargs):
    pass

def func3(pos1,pos2,*vargs,**kargs):
    print("func3 invoked")
    print("pos1 : ",pos1)
    print("pos2 : ",pos2)
    print("vargs : ",vargs)
    print("kargs : ",kargs)
    pass

def func4(pos1,*vargs,pos2):
    pass

def func7(pos1,pos2,**kargs):
    pass

def func8(pos1,pos2,*vargs):
    pass

# def func5(pos1,pos2,**kargs,*vargs):
#     pass
# 컴파일 오류

# def func6(pos1,**kargs,pos2):
#     pass  
# 선언부터 오류

# func4(1,2,3,4) 컴파일 오류
# func5(1,2,key=3,4,5) 오류

func3(1,2,3,4,name=3,key=123)
func7(1,2,name=3,key=123)
func8(3,4,5)


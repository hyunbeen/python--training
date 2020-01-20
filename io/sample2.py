#io/sample2.py
#c언어 
# int number = 키보드 입력
# switch(number){
#     case 1:
#     case 2:
#     case 3:
#     default:code:
# }

def func1():
    print('-func1() invoked')
    pass


def func1():
    print('-func1() invoked')
    pass


def func2():
    print('-func2() invoked')
    pass


def func3():
    print('-func3() invoked')
    pass


def func4():
    print('-func4() invoked')
    pass


def func5():
    print('-func5() invoked')
    pass


def func6():
    print('-func6() invoked')
    pass

def func7():
    print('-func7() invoked')
    pass

#파이썬에서 함수객체는 1급객체(First Class Object)
switch = {
    1:func1,
    2:func2,
    3:func3,
    4:func4,
    5:func5,
    6:func6,
    7:func7
    }
prompt = '''
                --------------------------------
                              menu
                --------------------------------
                        1. menu 1
                        2. menu 2
                        3. menu 3
                        4. menu 4
                        5. menu 5
                        ...
                        99. Quit 
                
                Select a number : '''

while(1):
    number = int(input(prompt))
    if(number==99):
        print("Quitting...")
        break
        pass
    # print("switch[%d]:"%(number),switch[number])
    switch[number]() #딕셔너리에 저장된 해당번호의 함수 호출
    
    pass
    


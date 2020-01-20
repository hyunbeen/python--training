#io/sample1.py

#invoke 호출하다
#return 값이 없는데 값을 받으면 None값을 받는다
#정의된 함수는 변수에 저장할 수 있다
#함수는 다른 함수의 매개변수로 전달가능하다
#함수는 다른 함수의 return 키워드의 반환값으로 지정이 가능하다
#함수를 저장한 변수나,함수명이나 같다
#C언어의 함수포인터의 개녕과 같다

def add_mul(a,b) : 
    print('-'*60)
    print(" - add_mul({},{}) invoked.".format(a,b))
    return (a+b,a*b)
    pass

def innerfunc(func,a,b):
    print('-'*60)
    print(" - innerfunc({},{},{}) invoked.".format(func,a,b))
    return(func(a,b))
    pass

def returnfunc(func):
    print('-'*60)
    print(" - returnfunc({}) invoked.".format(func))
    return func
    pass

func = add_mul #이함수의 주소를 가지고 있다
print('-'*60)
print(func)
print('-'*60)
# add,mul = func(3,4)
add,mul = innerfunc(func,3,4)
func2 = returnfunc(func)

print(type(add_mul))
print(id(add_mul))
print(add)
print(mul)
add,mul = func2(4,5)
print(add)
print(mul)

def make_list_for(num):
    print(" - make_list_for({}) invoked.".format(num))
    list = []
    for i in range(1,num+1):
        list.append(i)
    return list
    pass

list_num = make_list_for(5)
print(list_num)   

def make_list_comp(num):
    print(" - make_list_comp({}) invoked.".format(num))
    list = []
    list = [num for num in range(1,num+1)]
    return list
    pass

list_num = make_list_comp(5)
print(list_num)    

def make_list_comp_even(num):
    print(" - make_list_comp_even({}) invoked.".format(num))
    list = []
    list = [num for num in range(1,num+1) if ((num%2)==0)]
    return list
    pass

list_num = make_list_comp_even(10)
print(list_num) 

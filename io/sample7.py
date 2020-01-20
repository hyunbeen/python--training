#io/sample7.py

# 람다식 = Lamda expression
# 람다식의 목표 : 익명함수(Anonymous Function) 정의(선언)

#함수를 사용
def add(num1,num2):
    return num1+num2
    pass

print(add(3,4))

#람다를 사용

print("-"*60)
result = lambda num1,num2 : [num1+num2,num1*num2]

print(type(result))
print(result)
print(result(6,8))

#람다는 키워드이다 예시 for
#람다의 매개변수를 표현하고 싶어 
#lambda 뒤에 ()로 감싸면 무조건 오류
#람다는 값을 넣기 위한 용도 한줄용도로
# result = lambda num1,num2 : return num1+num2 오류

result = lambda num1,num2 : (num1+num2,num1*num2)
print(result(6,8))
result = lambda : 100
print(result())
result = lambda num1,num2 : print(num1+num2)
result(30,40)
print(result(30,40))
result = lambda num1,num2 : print(num1+num2);print(777)
print(result(30,40))
result = lambda num1,num2 : num1+num2;print(777)
print(result(30,40))
# result = lambda num1,num2 : print(num1+num2) 
#                             print(num1+num2) #두줄은 불가능하다
#print(a),print(b) 1 2 (None,None)
#print(a);pring(b) 1 2
#print(a,end="----------") and print(b,end="++++++++")가능
print("-"*60)

def plus_ten(x):
    return x + 10

print(list(map(plus_ten, [1, 2, 3])));

print("-"*60)

lam = lambda num1:num1+10 if num1 == 1 else num1 + 20 if num1 == 2 else num1 + 30 
print(list(map(lam,[1,2,3,4]))) 
print("-"*60)

def f(x):
    return x > 5 and x < 10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
b = list(filter(f, a))
print(b)

c = list(filter(lambda x: x > 5 and x < 10, a))
print(c)
print("-"*60)

lam = lambda x: x > 5 and x < 10
print(list(map(lam,[1,2,3,4,5,6,7,8,9,10]))) 
print("-"*60)
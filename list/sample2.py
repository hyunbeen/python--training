#list/sample2.py

a=1
print(type(a)) #출력타입은?

b=.56
print(type(b))

c='Yoesph'
print(type(c))

d=False
print(type(d))

e=[1,2,3,4,5]
print(type(e))

print('-----------------------------');
#파이썬에서는 base type의 변수이든 container type의 변수이든 모든 자료형(data type)의 값은 객체이다
str = 'Yoseph,Kim'
print(dir(str));
list = []
print(dir(list));
num = 1
print(dir(num));
print(type(type));
print(dir(int));
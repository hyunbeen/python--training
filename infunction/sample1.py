# print(abs(3))
# print(abs(-3))
# print(abs(-1.2))

# print(all([1, 2, 3]))
# print(all([1, 2, 3, 0]))

print(any([1, 2, 3, 0]))
print(any([0, ""]))

i = 97
while(1):
    if(chr(i)=='z'):
        print(chr(i),end="")
        break
    print(chr(i),end="")
    i += 1

print("\n",end="")

print(ord('a'))
print(ord('한'))
print(chr(54620)) #utf8 지원

print(divmod(7,3))

print(dir([1,2,3]))
for member in dir(str):
    print('{}'.format(member))

#dir은 모듈의 특성을 보여준다
#클래스의 속성과  반복해서 그속의 속성들의 속성을 보여준다
#객체의 속성과  반복해서 그속의 속성들의 속성을 보여준다

print(dir({'1','a'}))
print(eval('1'+'2'))

result = [1,2,3,4]
print(enumerate(result))
print(enumerate(result).__sizeof__())

# 빅데이터로 할수있는 연산작업을 크게 두가지로 나누면
# 1)map작업(형변환 작업 : 예 숫자형 텍스트 --> 숫자)
# 2)reduce작업 (Aggregation = 집계)
# 위 두개를 합쳐서 보통 "MapReduce" 라고 합니다
def multwo(num):
    return num * 2
generator = map(multwo,[1,2,3,4,5])
print(generator)
list1 = list(generator)
print(list1)
print("------------------------------")
print(generator)
list1 = list(generator)
print(list1)

#generator 객체인 맵
#특징은 일회성 값 제공, 반복형

print(list(zip([1, 2, 3, 4], [4, 5, 6, 7])))
z = range(1,5)
list1 = list(z)
print(list1)
list1 = list(z)
print(list1)

print(round(4.52342353252631341341,5))
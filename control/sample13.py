#control/sample13.py

a = [1,2,3,4,5]
b = list()
# for element in a:
#     b.append(element * 3) #append는 끝쪽에 insert는 앞에 붙인다
#     pass

a = [1,2,3,4]
# result = [num * 3 for num in a]
# result = [num for num in range(2,100001,2)]

# result = {num * 3 for num in (1,2,3,4)}

# result = set([num if (num % 2 == 0) else 0  for num in range(1,101,1)])
# result.remove(0)
# result = list(result)
# print(result)

# list comprehension
# generator 라는 타입의 객체가 생성됨
# 

listComprehension = []
tupleComprehension = ()
setComprehension = {}



listComprehension = [num * 3 for num in (1,2,3,4)]
print('-'*60)
print(listComprehension)
print(type(listComprehension))

tupleComprehension = (num * 3 for num in (1,2,3,4))
#tuple comprehension의 결과로 튜플이 생성되는 것이 아니라 generator가 생성이된다.
#generator는 1회용 값 생성기이다
print('-'*60)
print(tupleComprehension)
print(type(tupleComprehension))
print(tuple(tupleComprehension))
print(tuple(tupleComprehension)) #generator는 재사용이 안된다

setComprehension = {num * 3 for num in (1,2,3,4)}
print('-'*60)
print(setComprehension)
print(type(setComprehension))

result = [num for num in range(2,10,1) if(num % 2 == 0)]
result2 = [num for num in range(2,10,1) if(num % 2 == 0) if(num % 3 == 0)] #if문 여러번 가능하나 중첩 if문으로 적용

print('-'*60)
print(result)
print('-'*60)
print(result2)

#중첩포문으로 데이터를 넣을수 있다
result3 = [x*y for x in range(2,10)
               for y in range(1,10)]

#값을 다양한 형태로 넣을수 있다
result3 = [{x:y} for x in range(2,10)
               for y in range(1,10)]
print('-'*60)
print(result3)

#다양한 형태로 넣은 값을 뽑아 쓸수 있다
dictionary = dict(result3[0])
print(dictionary)
print(dictionary.get(2))

#여러번 넣고 싶을 경우
result4 = [x for x in range(2,10)]
result4 += [y for y in range(1,10)]
print(result4)

y=[12,13,14,15,16,17,18,19]
x=[2,3,4,5,6,7,8,9]

#enumerate 사용법 익히기
for index,value in enumerate(x) :
    print(x[index])
    print(y[index])



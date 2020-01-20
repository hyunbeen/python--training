from random import * #랜덤수를 입력받기위한 모듈호출

'''
logic : 자리수를 땐다
ex)
num = 723
one=num%10  --> 3
two=num//10%10 --> 2
three = num//100 --> 7
'''

list =[]; #입력받는 리스트
temp = [] #중간과정 정렬된 리스트

inputnum = int(input("입력받고 싶은 양수의 개수를 입력하시오 : ")) #입력받을 정수의 개수
maxnum = int(input("최대숫자의 범위를 입력하시오(1~999) : ")) #입력받을 숫자의 범위
type = int(input("오름차순과 내림차순을 결정하시오(0:오름차순 1:내림차순) : ")) #오름차순 내림차순 결정

mostlist = [] #최빈도 리스트
index = -1 #최빈도 리스트 인덱스
max = -1 #최빈도의 max값
comp = 0 #각 리스트 원소의 최빈도 값
sum = 0 #평균을 구하기 위한 합계변수
average = 0;
lislen = len(list) #리스트길이
k=0

start = 0 #오름차순 내림차순 정렬에 사용하는 변수
end = 0
inc = 0



#랜덤수 입력받기
for i in range(0,inputnum) :
    list.append(randint(1, maxnum))


#반복문 시작 마지막 결정
if(type == 0):
    start = 0
    end = 10
    inc = 1
elif(type == 1):
    start = 9
    end = -1
    inc = -1

#일의자리 정렬
for i in range(start,end,inc) :
    
    while(k!=len(list)):
        if list[k]%10 == i:
          
            temp.append(list[k])
            list.remove(list[k])
            
        else :
            k = k+1
    k=0


#임시 정렬된 리스트 저장 
list = temp
temp = []

#십의자리 정렬
for i in range(start,end,inc) :
   
    while(k!=len(list)):
        if list[k]//10%10 == i:
          
            temp.append(list[k])
            list.remove(list[k])
            
        else :
            k = k+1
    k=0

#임시 정렬된 리스트 저장 
list = temp
temp = []

#백의자리 정렬
for i in range(start,end,inc) :
   
    while(k!=len(list)):
        if list[k]//100 == i:
          
            temp.append(list[k])
            list.remove(list[k])
            
        else :
            k = k+1
    k=0

#임시 정렬된 리스트 저장 
list = temp


#총합과 최빈수 구하기
for i in range(0,len(list)) :
    
    comp = list.count(list[i])
    sum += list[i]
    
    if(max==comp):#최빈수가 여러개 존재할시에
        if(mostlist.count(list[i])==0) :#다른 최빈수 일경우에 추가
            mostlist.append(list[i]);
    elif(max<comp):#새로운 최빈수가 나타났을때
        max = comp
        mostlist = [];
        mostlist.append(list[i]);

average = sum/len(list) #평균


if(type == 0) :
    print("오름차순 정렬된 정렬 : ",list)
    print("중위수 : ",list[lislen//2])
    print("최빈수 : ",mostlist)
    print("평균값 : ",average)
elif(type == 1) :
    print("내림차순 정렬된 정렬 : ",list)  
    print("중위수 : ",list[lislen//2])
    print("최빈수 : ",mostlist)
    print("평균값 : ",average)
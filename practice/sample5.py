#sample5.py

# 숫자 맞추기게임
# 범위 1~45
# 사용자가 입력한 값과 확인하여 맞출때까지 찾는다 
# 범위를 제공한다

'''
logic :

1~45
최소 : 1
최대 : 45
중간값 : 23
답 : 40
제공값 : 23 ~ 45

23~45
최소 : 23
최대 : 45
중간값  : 34 (23+45/2)
답 : 40
제공값 : 34 ~ 45

'''
import random

#최소값 입력
while(1):
    #값을 문자열로 입력 처리
    try :
        min = int(input("최소값을 입력해 주세요(1이상의 숫자를 입력해 주세요) : ")) #최소범위
    except ValueError : 
        print("오류값을 입력하셨습니다")
        continue
        pass
    #값의 범위 오류 처리
    if (min<1) :
        print("범위를 벗어났습니다")
        continue
        pass
    #올바로 입력한 경우
    break
    pass


#최대값 입력
while(1):
    #값을 문자열로 입력 처리
    try :
        max = int(input("최대값을 입력해 주세요(최소값 이상인 숫자를 입력해 주세요) : ")) #최대범위
    except ValueError : 
        print("오류값을 입력하셨습니다")
        continue
        pass
    #값의 범위 오류 처리
    if (max<min) :
        print("범위를 벗어났습니다")
        continue
        pass
    #올바로 입력한 경우
    break
    pass



question = random.randint(min, max) #문제를 랜덤으로 설정
middle = 0 #min과 max의 중간값
number = 0 #사용자가 제시한 값
count = 0 #답을 맞추는데 걸린 횟수

print("-"*65)
print("범위는 %d ~ %d 까지 숫자를 맞추는 게임입니다.".center(50,"-")%(min,max))
print("-"*65)


#값을 맞추기 시작
while(1):
   
    middle = round((min+max)/2) #중간값 변화
    
    
    #값을 문자열로 입력 처리
    try :
        number = int(input("숫자를 입력해 주세요 : "))
    except ValueError : 
        print("오류값을 입력하셨습니다")
        continue
        pass
   
    #값의 범위 오류 처리
    if (number<min) | (number>max) :
        print("범위를 벗어났습니다")
        continue
        pass
    
    #올바른 값을 입력한 경우
    print("-"*60)
    
    count += 1    #답을 입력한 횟수 증가

    if(question == number):#답을 맞춘경우
        print("답은 %d 입니다"%number)
        print("%d번만에 답을 찾았습니다."%(count))
        print("-"*60)
        break
        pass

    elif(middle>question) : #중간값이 답보다 작을경우
        print("틀렸습니다")
        print("범위는 {0} ~ {1} 까지 입니다.".format(min,middle))
        max = middle
        pass

    elif(middle<=question) :#중간값이 답보다 클경우
        print("틀렸습니다")
        print("범위는 {0} ~ {1} 까지 입니다.".format(middle,max))
        min = middle
        pass


    print("-"*60)



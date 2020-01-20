#io/sample9.py

#전자계산기 덧셈,뺄셈곱셈,나눗셈

#1.덧셈기능 구현
add = lambda num1,num2 : num1+num2
sub = lambda num1,num2 : num1-num2
mul = lambda num1,num2 : num1*num2
div = lambda num1,num2 : num1/num2
switch = [add,sub,mul,div]
prompt ='''
-----------------------------
         전자계산기
1.덧셈
2.뺄셈
3.곱셈
4.나눗셈
5.끝내기
-----------------------------

select number : '''

while(1):
    inputnum = int(input(prompt))
    
    if(inputnum==5):
        break
    elif((inputnum<=4)&(inputnum>=1)):
        num1 = int(input("첫번째 숫자를 입력해 주세요 : "))
        num2 = int(input("두번째 숫자를 입력해 주세요 : "))
        answer = switch[inputnum-1](num1,num2)
        print("결과는 : {}".format(answer))
    else:
        print("잘못된 입력값입니다") 

        





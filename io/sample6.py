# 전역변수와 지역변수의 유효범위
#전역변수의 유효범위
#프로그램의 실행이 종료될때 까지 유지되는 변수
#지역변수의 유효범위
#자기가 정의/선언된 함수블록 범위 내에서만 유지되는 변수
for v in [1,2,3]:
    v2 = v
    pass

if(True):
    v3 = 3
print(v)
print(v2)
print(v3)

while 1:
    v4 = True
    if(v4):
        break

print(v4)
print('-'*80)
a = 1#a:전역변수

def vartest(b):#b:지역변수
    global a
    global c 
    c = 1
    a = a + 1
    c += 1

vartest(3)

print(a)
print(c)

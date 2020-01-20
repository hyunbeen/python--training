#과제2
#입력받는 부분

cavedistance = int(input("동굴의 길이를 입력해주세요 : "))#동굴의 총길이

run = int(input("하루에 올라갈 수 있는 길이를 입력해주세요 : ")) #하루에 올라갈수 있는 길이

sleep = int(input("하루에 미끄러지는 길이를 입력해주세요 : ")) #잘때 미끄러지는 길이

#단순 계산 버전

# def findday(cavedistance,run,sleep):
#     day = cavedistance//(run-sleep)+1 
#     return day

# if run-sleep<=0 :
#     print("잠을 너무 많이자서 올라갈 수가 없습니다.")
# else:
#     print("동굴 {0}m까지 가는데 걸리는 날짜는 {1}일이다".format(cavedistance,findday(cavedistance,run,sleep)))

#반복문 버전

def findday(cavedistance,run,sleep):
    
    day = 0; #소요시간
    updistance = 0;#하루에 올라간 거리
    
    while(updistance<cavedistance):
        
        day += 1 
        updistance += (run-sleep)
      
    return day

if run-sleep<=0 :
    print("잠을 너무 많이자서 올라갈 수가 없습니다.")
else:
    print("동굴 {0}m까지 가는데 걸리는 날짜는 {1}일이다".format(cavedistance,findday(cavedistance,run,sleep)))
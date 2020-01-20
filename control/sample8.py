coffee = 10
allmoney = 0
while True :
    money = int(input("돈을 넣어 주세요 :"))
    allmoney += money
    if(coffee==0):
       print("커피가 다 소모 되었습니다.")
       allmoney = 0;
       print("잔액은 %d 입니다"%allmoney)
       break
    elif (allmoney > 300) :
        print("잔액은 %d 입니다"%(allmoney-300))
        allmoney = 0
        coffee -= 1
    elif (allmoney == 300):
        print("커피를 줍니다.")
        allmoney = 0
        coffee = coffee -1
    else :
        print('돈이 모자랍니다....')
        print("모자란돈은 %d 입니다"%(300-allmoney))
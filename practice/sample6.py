#여러 종류의 메뉴를 서비스하는 길거리 자판기를 만들자!!!
#자판기는 이용자가 제공한 금액과 선택한 메뉴대로 서비스 해야한다!!
#메뉴랑 돈을 입력받는다
#나간것은 프린트 한다
#지폐 단위는 상관없음
#거스름돈 500 100 50 10원


adminnumber = 1234
change = {"500":100,"100":100,"50":100,"10":100}
menucount = {"1":10,"2":10,"3":10,"4":10,"5":10,"6":10,"7":10}
menuprice = {"1":300,"2":300,"3":500,"4":500,"5":700,"6":1000,"7":1200}
menuname = {"1":"아메리카노(ice)","2":"아메리카노(hot)","3":"라떼(ice)","4":"라떼(hot)","5":"카라멜마끼야또(hot)","6":"코코팜요구르트","7":"사이다"}

typeprompt = '''
    ---------------------------
            select mode  
    ---------------------------
    1. 사용자모드
    2. 관리자모드
    3. 시스템 종료
    
    Select a number: '''

adminprompt = '''
    ---------------------------
         1team coffeshop  
    ---------------------------
    1. 수입된 돈 끄내기
    2. 거스름돈 넣기
    3. 재고추가
    4. 메뉴추가
    5. 메뉴삭제
    6. 돌아가기
    
    Select a number: '''

menuprompt = '''
    ---------------------------
                MENU
    ---------------------------
    1. 아메리카노(ice)     - 300
    2. 아메리카노(hot)     - 300
    3. 라떼(ice)           - 500
    4. 라떼(hot)           - 500
    5. 카라멜마끼야또(hot)  - 700
    6. 코코팜요구르트       - 1000
    7. 사이다              - 1200
    8. 주문
    9. 돌아가기

    Select a number: '''





def buyallmenu(totalbuymenu,buylist):
    for i in buylist :
        print("메뉴 : %s 구입개수 : %d"%(menuname[str(i[0])],i[1]))
        
    print("총결제 금액은 : %d"%(totalbuymenu))
    
    print("동전을 넣어주세요")

    input500 =  int(input("500원을 넣어주세요 : "))
    input100 =  int(input("100원을 넣어주세요 : "))
    input50 =  int(input("50원을 넣어주세요 : "))
    input10 =  int(input("10원을 넣어주세요 : "))

    inputmoney = input500 *500 + input100 *100 + input50 *50 + input10 *10

    if(totalbuymenu<=inputmoney):
        
        print("결제가 완료 되었습니다.")
        print("잔액은 %d원 입니다"%(totalbuymenu-inputmoney))
        
        change["500"] += input500
        change["100"] += input100
        change["50"] += input50
        change["10"] += input10

        if(totalbuymenu-inputmoney>0):
            print("잔액을 반환합니다")
            userchange = totalbuymenu-inputmoney
            money500 = 500
            money100 = 100
            money50 = 50
            money10 = 10
            user500 = 0
            user100 = 0
            user50 = 0
            user10 = 0

            if(userchange//500>0):
                user500 = userchange//500
                userchange -= user500 * 500 
                pass
            if(userchange//100>0):
                user500 = userchange//100
                userchange -= user500 * 100 
                pass
            if(userchange//500>0):
                user500 = userchange//500
                userchange -= user500 * 500 
                pass
            if(userchange//500>0):
                user500 = userchange//500
                userchange -= user500 * 500 
                pass
            pass        
        pass
    else:
        print("돈이 부족합니다.반환합니다")
        pass
    pass



#메뉴 구입 화면
def showmenu():
    totalbuymenu = 0
    buylist = []
    while(1):
        buynum = int(input(menuprompt))
        if(buynum==9):
            break
            pass
        elif((buynum>=1)and(buynum<=7)):
            
            totalbuymenu,buylist = buymenu(buynum,totalbuymenu,buylist)
            pass
        elif(buynum==8):
            buyallmenu(totalbuymenu,buylist)
            pass
        pass
    pass

def buymenu(buynum,totalbuymenu,buylist):
    
    menucount = int(input("개수를 입력해주세요 : "))
    name = menuname[str(buynum)]
    totalprice = menuprice[str(buynum)] * menucount
    print("구매정보입니다")
    print("주문메뉴 : %s 주문수량 : %d 총가격 : %d"%(name,menucount,totalprice))
    totalbuymenu += totalprice;
    buylist.append([buynum,menucount])
    return totalbuymenu,buylist
    pass

#메뉴추가 
def addmenu():
    for len(menuname)
    pass

#시작화면
def init():
    money = change["500"]*500 + change["100"]*100 + change["50"]*50 + change["10"]*10
    while(1):
        initnum = int(input(initprompt))

        if(initnum == 1):
            password = int(input("관리자 번호를 입력해 주세요 : "));
            if(password == adminnumber):
                print("총 수입된 금액입니다 : %d"%(money))
                change["500"] = 0
                change["100"] = 0
                change["50"] = 0
                change["10"] = 0 
                money = 0
            else:
                print("번호가 틀렸습니다")
                print("이전화면으로 돌아갑니다")
            pass

        elif(initnum == 2):
            print("500원 : %d,100원 : %d,50원 : %d,10원 : %d"%(change["500"],change["100"],change["50"],change["10"]))
            print("추가할 돈의 개수를 입력해 주세요")
            num500 = int(input("추가할 500원의 개수 : "))
            num100 = int(input("추가할 100원의 개수 : "))
            num50 = int(input("추가할 50원의 개수 : "))
            num10 = int(input("추가할 10원의 개수 : "))
            print("추가중입니다...")
            print("현재 잔돈의 수")
            change["500"]+=num500
            change["100"]+=num100
            change["50"]+=num50
            change["10"]+=num10
            money = 500 * change["500"] + 100 * change["100"] + 50 * change["50"] + 10 * change["10"] 
            print("500원 : %d,100원 : %d,50원 : %d,10원 : %d"%(change["500"],change["100"],change["50"],change["10"]))
            pass

        elif(initnum == 3):
            showmenu();
            pass
        
        elif(initnum == 4):
            
            pass
        elif(initnum == 5):
            addmenu()
            pass
        elif(initnum == 6):
            deletemenu()
            pass
        elif(initnum == 7):
            print("프로그램이 종료됩니다")
            break

        pass    

init()
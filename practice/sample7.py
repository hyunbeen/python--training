adminnumber = 1234

change = {"10000":100,"5000":100,"1000":100,"500":100,"100":100,"50":100,"10":100}
menucount = [10,10,10,10,10,10,10]
menuprice = [300,300,500,500,700,1000,1200]
menuname = ["아메리카노(ice)","아메리카노(hot)","라떼(ice)","라떼(hot)","카라멜마끼야또(hot)","코코팜요구르트","사이다"]
totalcount = 0

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
    6. 비밀번호 바꾸기
    7. 돌아가기
    
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


def init():
    
    while(1):
        inputnumber = int(input(typeprompt))
        if(inputnumber==3):
            break
            pass
        elif(inputnumber==1):
            usermode()
            pass    
        elif(inputnumber==2):
            password = int(input("관리자 번호를 입력해 주세요 : "))
            if(password == adminnumber):
                adminmode()
                pass
            else:
                print("잘못된 입력입니다.")
                pass
            pass
        else:
            print("잘못된 입력입니다")
            pass
        pass

def showlist():
    print('-----------------------------------------------')
    print('                      menu                     ')
    print('-----------------------------------------------')          
    for i in range(0,len(menuname)):
        print(i,".",menuname[i],"------------",menuprice[i],'원')

def showlistcount():
    print('-----------------------------------------------')
    print('                      menu                     ')
    print('-----------------------------------------------')          
    for i in range(0,len(menuname)):
        print(i,".",menuname[i],"------------",menucount[i],'개')

def showlistmenu():
    print('-----------------------------------------------')
    print('                      menu                     ')
    print('-----------------------------------------------') 
             
    for i in range(0,len(menuname)):
        print(i,".",menuname[i],"------------",menuprice[i],'원')
        pass
    print(len(menuname),".",'주문')        
    print(len(menuname)+1,".",'돌아가기')        

def adminmode():
    
    while(1):
        
        inputnumber = int(input(adminprompt))

        if(inputnumber==7):
            break
            pass
        elif(inputnumber==1):

            totalmoney = change["10000"]*10000 + change["5000"] * 5000 + change["1000"] * 1000 + change["500"] * 500 + change["100"] * 100 + change["50"] * 50 + change["10"] * 10
        
            print("총 수입된 금액입니다 : %d"%(totalmoney))
        
            change["10000"] = 0
            change["5000"] = 0
            change["1000"] = 0
            change["500"] = 0
            change["100"] = 0
            change["50"] = 0
            change["10"] = 0 

            pass
        elif(inputnumber==2): 

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
           
            print("500원 : %d,100원 : %d,50원 : %d,10원 : %d"%(change["500"],change["100"],change["50"],change["10"]))

            pass
        elif(inputnumber==3):
            while(1):
                showlistcount()
                
                inputnumber = int(input("추가할 메뉴의 번호를 눌러주세요 : "))
                count = int(input("추가할 수량을 눌러주세요 : "))
                
                menucount[inputnumber] += count

                print("추가가 완료됬습니다")
                showlistcount()
                inputnumber = int(input("추가를 끝내시려면 숫자 0을 눌러 주세요 : "))
                
                if(inputnumber == 0):
                    break
                    pass

                pass
            pass
        elif(inputnumber==4):
            while(1):
                showlist()
                
                name = input("추가할 메뉴의 이름을 눌러주세요 : ")
                price = int(input("추가할 메뉴의 가격 눌러주세요 : "))
                count = int(input("추가할 메뉴의 수량을 눌러주세요 : "))

                menuname.append(name)
                menuprice.append(price)
                menucount.append(count)

                print("추가가 완료됬습니다")
                showlist()
                inputnumber = int(input("추가를 끝내시려면 숫자 0을 눌러 주세요 : "))
                
                if(inputnumber == 0):
                    break
                    pass

                pass
            pass
        elif(inputnumber==5):
            while(1):
                showlist()
        
                count = int(input("삭제할 메뉴 번호를 눌러주세요 : "))

                menuname.pop(count)
                menuprice.pop(count)
                menucount.pop(count)

                print("삭제가 완료됬습니다")
                showlist()
                inputnumber = int(input("삭제를 끝내시려면 숫자 0을 눌러 주세요 : "))
                
                if(inputnumber == 0):
                    break
                    pass

                pass
            pass
        elif(inputnumber==6):
            adminnumber = int(input("변경될 관리자 번호를 입력해 주세요 : "))
            pass
        else:
            print("잘못된 입력입니다")
            pass
        pass

def usermode():
        totalmoney = 0
        totallist = []
        while(1):
            showlistmenu()
            inputnumber = int(input("select number : "))
            if(inputnumber==len(menuname)+1):
                break
                pass
            elif(inputnumber==len(menuname)):
                print("----------------------------------------------------------")
                print("                         주문정보                          ")
                print("----------------------------------------------------------")
                for i in totallist :
                    print("%s(%d원)         %d개           %d"%(i[0],i[1],i[2],i[3]))
                pass
                print("결제금액 : %d"%(totalmoney))
                print("----------------------------------------------------------")
                print("돈을 넣어주세요")
                input10000 = int(input("10000원 개수를 입력해주세요 : "))
                input5000 = int(input("5000원 개수를 입력해주세요 : "))
                input1000 = int(input("1000원 개수를 입력해주세요 : "))
                input500 = int(input("500원 개수를 입력해주세요 : "))
                input100 = int(input("100원 개수를 입력해주세요 : "))
                input50 = int(input("50원 개수를 입력해주세요 : "))
                input10 = int(input("10원 개수를 입력해주세요 : "))

                totalinput = (input10000*10000)+(input5000*5000)+(input1000*1000)+(input500*500)+(input100*100)+(input50*50)+(input10*10)
                
                if(totalinput > totalmoney):
                    
                    changemoney = totalinput-totalmoney
                    change500 = 0
                    change100 = 0
                    change50 = 0
                    change10 = 0
                    print("잔돈은 %d원입니다"%(changemoney))
                    if(changemoney//500<=change["500"]):
                        change500 = changemoney//500
                        changemoney -= (changemoney//500)*500
                        
                    else:
                        changemoney -= change["500"]*500
                        change500 = change["500"]

                    if(changemoney//100<=change["100"]):
                        change100 = changemoney//100
                        changemoney -= (changemoney//100)*100
                        
                    else:
                        changemoney -= change["100"]*100
                        change100 = change["100"]
                    

                    if(changemoney//50<=change["50"]):
                        change50 = changemoney//50
                        changemoney -= (changemoney//50)*50
                        
                    else:
                        changemoney -= change["50"]*50
                        change50 = change["50"]
                    

                    if(changemoney//10<=change["10"]):
                        change10 = changemoney//10
                        changemoney -= (changemoney//10)*10
                        
                    else:
                        changemoney -= change["10"]*10
                        change10 = change["10"]
                    
                    if(changemoney!=0):
                        print("잔돈을 전체 반환할수 없습니다")
                        print("입력한 금액을 전체 반환합니다")
                        pass
                    else:
                        change["500"]-=change500
                        change["100"]-=change100
                        change["50"]-=change50
                        change["10"]-=change10
                        # finish = 0
                        # for i in totallist :
                        #     if(i[2]>menucount[i[4]]):
                        #         finish = 1
                        #         break
                        #     # print("%s(%d원)         %d개           %d"%(i[0],i[1],i[2],i[3]))
                        # pass
                        # if(finish)
                        print("500원 : %d 100원 : %d 50원 : %d 10원 : %d"%(change500,change100,change50,change10))
                        print("결제완료") 
                        pass
                    pass
                elif(totalinput == totalmoney):
                    print(2);
                    print("잔돈이 없습니다")
                    change["10000"]+=input10000
                    change["5000"]+=input5000
                    change["1000"]+=input1000
                    change["500"]+=input500
                    change["100"]+=input100
                    change["50"]+=input50
                    change["10"]+=input10
                    print("결제완료")  
                    pass
                else:
                    print(3);
                    print("돈이부족하여 전체 입금액이 환불됩니다")

                  
            elif((inputnumber>=0)&(inputnumber<len(menuname))):
                count = int(input("구매할 개수를 입력해 주세요 : "))
                totalmoney += menuprice[inputnumber] * count
                emptylist = []
                emptylist.append(menuname[inputnumber])
                emptylist.append(menuprice[inputnumber])
                emptylist.append(count)
                emptylist.append(menuprice[inputnumber] * count)
                emptylist.append(inputnumber)
                totallist.append(emptylist)
                pass
            else:
                print("잘못된 입력입니다.")
                pass
            pass
      
        
    

init()
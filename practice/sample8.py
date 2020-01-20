import random

randomList = []      # 랜덤 리스트
change = 0                                                                                                                                                 
mostList = [] #최빈수 리스트
                                           
# writefile = open("C:/app/py_workspace/io/file/sort.txt", 'w') #결과값 정보를 기억
writefile = open("C:/sort.txt", 'w') #결과값 정보를 기억
inputnum = int(input("입력받고 싶은 양수의 개수를 입력하시오 : ")) #입력받을 정수의 개수
maxnum = int(input("최대숫자의 범위를 입력하시오 : ")) #입력받을 숫자의 범위
type = int(input("정렬을 설정하시오(0:오름차순 1:내림차순) : "))#오름차순 내림차순 결정


#--------------------------------------------------------------------------------------------------------------------------

#랜덤수 입력받기
def initList(inputnum):
    makeList = []
    for i in range(0,inputnum) :
        makeList.append(random.randint(1, maxnum))
    pass
    return makeList
    pass

#정렬하기
def bubbleSort(randomList,randomListNum,type):
    
    for nextNum in range(randomListNum-1, 0, -1):
        for newListNum in range(0, randomListNum - 1, 1):
            if(type==0): #오름차순 정렬
                if (randomList[newListNum] > randomList[newListNum+1]):
                    randomList[newListNum],randomList[newListNum+1] = randomList[newListNum+1],randomList[newListNum]
                    pass
            pass
                
            if(type==1): #내림차순 정렬
                if (randomList[newListNum] < randomList[newListNum+1]):
                    randomList[newListNum],randomList[newListNum+1] = randomList[newListNum+1],randomList[newListNum]
                    pass
            pass
        pass
    pass
    
    return randomList

    

#최빈수 리스트 
def findMostList(**kargs):
  
    randomList = list(kargs.get("randomList"))
    randomListNum = int(kargs.get("randomListNum"))
    setList = list(set(randomList)) #중복값이 제거된 리스트
    mostList = []
    max = -1

    for i in setList :
        
        comp = randomList.count(i)
     
        if(max==comp):#최빈수가 여러개 존재할시에

            # if(mostList.count(randomList[i])==0) :#다른 최빈수 일경우에 추가
            #     mostList.append(randomList[i])
            #     pass

            mostList.append(i)
            pass
        elif(max<comp):#새로운 최빈수가 나타났을때
            max = comp
            mostList = [];
            mostList.append(i)
            pass

        pass
    return mostList,max
    pass

#합계를 구하는 함수
def findSumList(*vargs):
  
    randomList = list(vargs[0])
    randomListNum = int(vargs[1])
    sum = 0

    for i in range(0,randomListNum) :
        sum += randomList[i]
    pass

    return sum

#-----------------------------------------------------------------------------------------------------------------

randomList = initList(inputnum) #초기리스트 생성
randomListNum = len(randomList) #리스트의 길이
randomList = bubbleSort(randomList,randomListNum,type) #리스트 정렬

mostList,freq = findMostList(randomList=randomList,randomListNum=randomListNum) #최빈도 리스트와 그 빈도를 반환
listSum = findSumList(randomList,randomListNum) #리스트의 전체 합을 반환

findAverage = lambda listSum,randomListNum:listSum/randomListNum #람다를 이용한 평균구하기
average = findAverage(listSum,randomListNum) 

#중간값을 반환하는 람다식
findMedian = lambda randomList,randomListNum : (randomList[randomListNum//2]+randomList[(randomListNum//2)-1])/2 if((randomListNum%2)==0) else randomList[(randomListNum//2)]
median = findMedian(randomList,randomListNum)


#출력및 파일에 기록

if(type == 0) :
    print("오름차순 정렬된 정렬 : ",randomList)
    print("중위수 : ",median)  
    print("최빈수 : ",mostList,"빈도값 : ",freq)
    print("평균값 : ",average)
    writefile.write("오름차순 정렬된 정렬 : "+str(randomList)+'\n')
    writefile.write("중위수 : "+str(median)+'\n')
    writefile.write("최빈수 : "+str(mostList)+" 반복된 횟수 : "+str(freq)+'\n')
    writefile.write("평균값 : "+str(average)+'\n')
elif(type == 1) :
    print("내림차순 정렬된 정렬 : ",randomList)  
    print("중위수 : ",median)
    print("최빈수 : ",mostList,"빈도값 : ",freq)
    print("평균값 : ",average)
    writefile.write("내림차순 정렬된 정렬 : "+str(randomList)+'\n')
    writefile.write("중위수 : "+str(median)+'\n')
    writefile.write("최빈수 : "+str(mostList)+" 반복된 횟수 : "+str(freq)+'\n')
    writefile.write("평균값 : "+str(average)+'\n')

writefile.close()


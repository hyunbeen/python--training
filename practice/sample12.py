# data = {1,2,3,4,5,6,7,8,9,10}
# for i in data :
#     print(i)

# for i in range(2,9,2) :
#     print(i,"단")
#     for j in range(1,10):
#         print(i,"*",j,"= ",i*j)

# A=3 
# B=2
# A,B = B,A
# print(A,B)

# def func1():
#     print("func1")

# def func2():
#     print("func2")

# def func3():
#     print("func3")

# switch = [func1,func2,func3]

# prompt = '''
# 번호를 입력해주세요 : '''

# while(1):
#     inputnum = int(input(prompt))
#     if(inputnum == 3):
#         break
#     elif(inputnum<=2 & inputnum>=1):
#         switch[inputnum]()
#     else:    
#         print("잘못된 입력입니다")

# I=[1,2,3,4,5,6,7,8,9,10]
# condition = lambda x : False if((x%2)==0) else True
# list = list(filter(condition,I))
# print(list)
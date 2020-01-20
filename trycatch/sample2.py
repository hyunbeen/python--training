try:
    # f = open("C:/app/py_workspace/trycatch/sample1.py","r")
    
     
    #  4/0 #error 발생순서의 따라 발생
     f = open("../py_workspace/trycatch/sample3.py","r")
     f = open("../py_workspace/trycatch/sample1.py","r") #워크 스페이스 기준
    #상대경로,절대경로 가능
except FileNotFoundError as e:
    print(e)
    # d = 3
    # print("확인")
    # print(dir(e))
    # print(type(e))
    # print(e.filename)
    # print(e.filename2)
    # print(e.errno)
    f = None
except ZeroDivisionError as e:
    print(e)
    f=None
finally:
    print("fianlly")
    # print("f : ",f) #f는 전역변수로 선언
    # print("d : ",d) #d는 전역변수로 선언
    if(f):
        f.close()

# print("f : ",f) #f는 전역변수로 선언
# print("d : ",d)


#try -> except -> finally (실행순서,코드기입순서)
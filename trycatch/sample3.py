
try:
    # num = int(input())
    a = [1,2,3]
    
    
    f = open("../py_workspace/trycatch/sample3.py","r")
    a[3]
    4/0
    pass
except(IndexError,FileNotFoundError,ZeroDivisionError)as e:
    
    if isinstance(e,FileNotFoundError):
        print("파일오류")
        f = None
    print(e)
    pass
except(ValueError):
    print("Value Error 입니다")
finally:
    if(f):
        f.close()
    pass
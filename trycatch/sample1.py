#   try{
#         코드1...코드N
#    }catch(예외명 변수명){
#       예외처리코드들...
#    }finally{
#       예외가 발생하든 발생하지 않든 반드시 수행
#    }

# with open('파일경로','파일모드')as f:
#      파일조작코드
#      pass

try:
    4/0
    pass
except (FileNotFoundError,ZeroDivisionError)as zero:
    print(type(zero))
    print(dir(zero))
    print(zero)
    print(type(zero.__str__))
    print(zero.__str__)
    print(zero.__str__())

    pass
finally:
    print("확인2")
    pass
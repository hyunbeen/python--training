#함수의 유효범위
#Local variable,Global variable
globalVar = 1

def vartest(localVar):
    localVar = localVar + 1
    localVar2 = "Yoesph"
    pass

vartest(globalVar)

print(globalVar)
# print(localVar) 실행은 되지만 오류가 발생한다
# 문법이 잘못된것은 Syntax Error 실행도중에 발생한 것은 runtime error 또는 실행 오류



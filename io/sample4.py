#io/sample4.py
def add_mul(a,b) : 
    print('-'*60)
    print(" - add_mul({},{}) invoked.".format(a,b))
    return (a+b,a*b)
    pass

(var1,var2) = (1,2)
print(var1,var2)

def say_myself(name, old, man=True): 
    print("- say_myslef({},{},{})".format(name,old,man))
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

#기본값이 정해진것은 뒤로 뺀다

say_myself("박응용", 27)
say_myself("박응용", 27, False)



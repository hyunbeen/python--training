#sample6.py
print(1 in {1:'가',2:'나',3:'다'})

pocket = {"money":3000}

print("-"*60)

if("money" in pocket ) : 
    print("택시를 타라")
    pass
else :
    print("걸어가라")
    pass

print("-"*60)

pocket = ['paper','cellphone','IDcard']
card = True
if ('money' in pocket) : #돈이 있다면
    #코드1
    #코드2
    pass
elif(card) : #카드가 있다면
    #코드1
    #코드2
    pass
elif ('IDcard' in pocket) : 
    #코드1
    #코드2
    pass
else : #돈도 없고 카드도 없다면
    #코드1
    #코드2
    pass

print("-"*60)

number = 80

if (number < 70) : 
    print("D등급")
elif (number < 80) :
    print("C등급") 
elif (number < 90) :
    print("B등급")
else :
    print("A등급")
print("-"*60)

score = 60
message = "success" if score >= 60 else "failure"
print(message)

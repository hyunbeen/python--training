#control/sample35.py

marks = [90,25,67,45,80]

# for number in range(len(marks)):
#     if marks[number]<60:
#         continue
#     print("%d번 학생 축하합니다. 합격입니다.%s" % (number+1,'바보'),"바보입니다%s"%("확인"))

a = range(0,10,2)

# print(type(a))
# print(a[3])
# print(a[1:3])
# print(id(a))
# print(a)

b = True

c = list(a)

d = range(-5,-1)

e = list(d)

# f = range(0,1,0.1)

#f = range(1.0,3.0) floating number은 안됩니다

for i in range(3,10,2) :
    print("-%d단-"%(i))
    for j in range (1,10,1):
        print("%d * %d = %d"%(i,j,i*j))
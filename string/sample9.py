#sample14.py
#문자열 포맷팅
print("I eat {0} apples and {1} grapes amd {2} oranges".format(3,4,2));
print("String {} {}".format(1,2))
print("String {second} {first}".format(first=3,second=10))
print("String {day}{0}{1}".format(1,3,day=20))
print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:*<10}".format("hi"))
print("{0:*>10}".format("hi"))
print("{0:*^10}".format("hi"))
y = 3.42134234
print("{:0.4f}".format(y))
print("{:^10.4f}".format(y))

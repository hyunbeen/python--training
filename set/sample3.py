import copy

a = [1,2,3]
b = a
b[0]=2
print(a)

a = [1,2,3] #deep copy
b = a[ : ]
b[0]=2
print(a)

c=[1,2]
d=copy.copy(c)
print(c is d)
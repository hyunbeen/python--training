import copy 
a = [1,2,3]
b = copy.copy(a)
b[0] = 4
print(a)
print(id(a))
print(id(b))
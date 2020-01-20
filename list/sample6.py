#list/sample6.py
a = [1,2,3,1,1]

#count
print(a.count(1));

#pop
a.pop(3);
print(a);
print(a.count(1));

#extend
a.extend([7,8,9]);
print(a); #a = a+ [7,8,9]



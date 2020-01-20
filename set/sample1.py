#sample1.py

s1 = set(['hello','hi'])
print(s1)
# print(s1[0]) 집합에는 순서가 없다

s2 = set('123');
print(s2)

s3 = set(dict()) #r공집합

s4 = {}
s4 = {1,2,3,1,2,3,'1','2','3'}
print(s4);

t1 = tuple(s4)
print(t1[3])
l1 = list(s4)
print(l1[4])

list1 = [1,2,3,1,2,3,4,'b','a','b']
temp = list(set(list1))
print(temp)
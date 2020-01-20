#set/sample2.py
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
#왼쪽을 기준객체 오른쪽을 비교개체
#순서를 보장하지 않는다

print(s1&s2)
print(s1.intersection(s2))
print(s1|s2)
print(s1.union(s2))
print(s1-s2)
print(s1.difference(s2))

#원소를 추가
s1.add(7)
print(s1)
s1.update([8,9,10,11])
s1.update([8,9,10,11,(111,222)]) #list의 list는 되지 않는다
print(s1)
s1.remove(9);
print(s1)
s1.update((12,13))
print(s1)
s1.update({14,15})
print(s1)
s1.update((16,(17,18)))
print(s1)
s1.update({10000:"1",20000:"2"}) #key값만 들어간다
print(s1)
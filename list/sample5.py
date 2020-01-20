#list/sample5.py
a=[1,2,3]
a[-1] = 100
a[0] = True
# del a[1],a[2] 리스트 삭제하면서 땡겨진다
#del a[1:] 가능
a.append(4)
print(a)
a.append(5)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
# print(a.index(11)) 오류
a = [1,2,3]
a.insert(0,4)
print(a)
a.remove(4)
print(a)
a.pop()
print(a)
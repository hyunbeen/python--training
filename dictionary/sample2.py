#dictionary/sample2.py

dic = {'name':'Yoesph','age':24}
dic['tel']='01027626623'
# dic['innerdic']={}
dic['innerdic']=dict()
dic['age']=18
dic[(1,2,3)]=18

print(type(dic))
print(id(dic))
print(len(dic))
print(dic[(1,2,3)])
del dic['innerdic'];

dic2 = {1:'value1',1:'value2'}
print(len(dic2))

dic3 = {"name":"lee","value":"been"}
# print(dic3[0])

for i in dic3.values() :
    print(i) 

print(list(dic3.values())[0])#list화 하여서 사용한다

print(dic3.items());

dic3items = list(dic3.items())
print(dic3items)
dic3itemstuple = tuple(dic3items[0]);

for (key,val) in dic3.items() :
    print(key)
    print(val)

t = (1,2)
(v1,v2)=t
print(v1)
print(v2)
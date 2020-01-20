#sample1.py
dic = {
        'name':'pey',
        'phone':'011199933323',
        'birth':'1118',
        8:[1,2,3]
    }

print(dic[8])
print(dic.keys())
print(dic.values())
print(dic.items())
dic.clear()
print(dic)
print(dic.get("phone"))
print(dic.get("foo","bar"))



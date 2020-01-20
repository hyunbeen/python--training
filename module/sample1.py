#module/sample1.py

#To use python module 'mod1'

import mod1 as m1
#from<모듈명>import <모듈안에 선언되어있는 멤버들>


print(dir(m1))
print(type(m1.ModClass()))

obj = m1.ModClass()
print(obj)

print(obj.staticField)
print(obj.instanceField)
print(obj.confirm)
print(obj.method1())


print(__name__)

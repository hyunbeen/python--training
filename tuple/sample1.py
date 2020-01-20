#tuple/sample1.py

#튜플은 요소를 변경이 되지 않는다
t0 = (1,);
print(type(t0)); #,가 들어가야 튜플
t1 = (1,2,'a','b')
print(type(t1));

print(t1[0]);
print(t1[0:2]);
print(t1*2);
print(len(t1));
print(1 in t1);
print(t1[-1]);

def add(a,b):
    return a+b;
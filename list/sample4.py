#list/sample4.py

#리스트 연산
a=[1,2,3,4,5]
b=[5,7,8,9,10]

# -,/ 연산은 지원되지 않는다
print("---------------------------------------------");
result = a + b
print(result)
result = a * 2
print(result)
leng = len(result)
print(leng)

# print(a[3]+"hi"); error 강제 형변환 시켜야된다
print("---------------------------------------------");
print(str(a[3])+"hi")
print("---------------------------------------------");
result = str(1)
print(result)
result = str(1.23)
print(result)
result = str(True)
print(result)
result = str([1,2,3])
print(result)
result = str("abc");
print(result)
print("---------------------------------------------");
result = int('1')
print(result)
result = float('1.23')
print(result)
result = bool('True')
print(result)
print("---------------------------------------------");
result = bool(1)
print(result)
result = bool(0)#'0'은 True
print(result)
result = bool(999)
print(result)
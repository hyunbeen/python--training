#io/sample11.py
#r,w,a,b
#read,write,append,binary
#운영체제의 파일시스템의 파일의 종류는 크게 두가지로 나뉜다
#text-based file
#byte based file(이진파일)

f = open("C:/app/py_workspace/io/file/line.txt", 'a')

# f = open("C:/app/py_workspace/io/file/read.txt", 'r')
# f = open("io/file/line.txt", 'w')
print(type(f))
print(id(f))
print(f)
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    
    f.write(data)
f.close()
f = open("C:/app/py_workspace/io/file/line.txt", 'r')


# line = f.readline()
# while True:
#     line = f.readline()
#     if not line: 
#         print(line) 
#         break
#     print(line)




# lines = f.readlines()
# for line in lines:
#     print(line)

data = f.read()
print(data)

f.close()

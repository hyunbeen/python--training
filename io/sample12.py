#io/sample12.py
#경로(path) 
#상대경로(Relative Path) : 현재 위치하는 폴더를 기준(C:/Tensorflow)으로 C:/Tensorflow/graph를 찾을때
#./graph  자식 디렉토리
#graph  자식 디렉토리
#../ or .. 부모 디렉토리
#절대경로(Absolute Path) 예: C:/Tensorflow/graph

#문자집합(character set)
#바이트(byte)컴퓨터에서 데이터를 메모리에 저장 및 표현하는 최소단위
#메모리 그 크기만큼의 바이트의 개수로 구성
#문자집합 - 각 나라의 언어마다, 표현가능한 모든 문자를 여러바이트를 이용해서, 이미 정해놓은 테이블
#예1)영어권을 위한 문자집합 --> ISO-8859-1(ASCII)
#예2)대한민국을 위한 문자집합 -->EUC-KR -->KSC5601
#예3)모든나라의 문자들을 표시할 수 있는 문자집합 --> UTF-8
#예4)윈도우 운영체제의 기본 문자집합 -->MS949(=CP949)

# 디코드(decode)/인코드(encode)

# f = open('data.txt','r',encoding='utf8')
# file = f.read()
# print(file)

#  * 0 -- start of stream (the default); offset should be zero or positive
#  * 1 -- current stream position; offset may be negative
#  * 2 -- end of stream; offset is usually negative
# f.seek(0)

# file = f.read()
# print(file) 
#더이상 안 읽힌다 -> 
# EOF(End Of File) 파일의 끝을 표시하는 특수문자 
# 눈으로 보이지 않기 때문에 특수문자
# ASCII 문자집합 테이블에 정의되어있는 특수문자
# 프로그램 코드가 파일을 열고 파일의 처음부터 읽다가, 
# EOF를 만나면 끝을 인식하고 읽는것을 끝낸다
# f.close()
#-----------------------------------------------------
f = open('line.txt','r')
# line = f.readline()
# line = f.readline()
# line = f.readline()
# line = f.readline()
# line = f.readline()
# line = f.readline()
# line = f.readline()
# line = f.readline()
# line = f.readline()
# line = f.readline()
# line = f.readline()
# print(type(line))
# print(len(line))

# while True:
#     line = f.readline()
#     if(line == ''): #EOF
#         break
#         pass
#     print(line,end="")
# f.close()
#-----------------------------------------------------
# f = open('data.txt','r',encoding='utf8')

# while True:
#     inputData = input("입력하세요 : ")
#     print(type(inputData))
#     if not inputData:
#         break
# f.close()
#-----------------------------------------------------
# f = open('line.txt','r')
# lines = f.readlines()
# print(type(lines))

# for line in lines:
#     print(line.replace("\n",""))

#module(pprint) pp.pprint() -> 문자열 정리

f = open('line.txt','a')

for i in range(11,21):
    f.write(str(i)+"번째 줄입니다.\n")
f.close()


#적극권장 : 열려진(사용한) 자원을 파이썬 인터프리터가 책임지고 닫아주기 때문에
#(블록내에서 오류가 발생하든/안하든),적극적으로 사용해야 함!!
with open("data.txt",'a',encoding='utf8') as f :
    f.write('\n')
    f.write('Append-7')
    f.write('\n')
    f.write('Append-8')
    pass
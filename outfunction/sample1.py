import pickle as pk
f = open('obj.dat','wb')

object = [1,2,3,4,5]
pk.dump(object,f)


f.close()

f = open('obj.dat','rb')
#지정된 파일에 저장되어있는 
#파이썬 객체를 현재의 실행 메모리로 다시불러들이는(loading)
data = pk.load(f)
print(data)

#객체의 직렬화(Serialization)
#->메모리에 생성되어 있는 객체를 파일등에 저장하기 위해
#일련의 바이트열로 변환하는 작업
#(Object -> Byte Sequence)
#객체의 역직렬화(De-Serialization)
#(Byte Sequence -> Object)
#data = [1,2,3,...100]
#f.write('1')f.write(',')훨씬더 효과적

#os.environ
#os.chdir
#os.getcwd()
#os.system("dir")

#byte로 형변환
#bytes("임시데이터","utf8")
#"임시데이터2".encode('utf8')
# f.write(b'임시데이터3')
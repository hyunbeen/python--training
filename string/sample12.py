#sample17.py
#문자열 객체의 여러 메소드 

string = "hobby"

#지정된 문자의 개수
print("----------------------------------");
print(string.count('b'))

string = "Python is the best choice"

# 지정된 문자의 처음나온 인덱스 번호를 찾아준다
print("----------------------------------");
print(string.find('b'));
print(string.find('k'));
print(string.find('best'));

# find와 동일하게 문자/문자열 위치를 찾아준다
print("----------------------------------");
print(string.index('b'));
#print(string.index('k')); 에러 발생

# 문자열의 각사이에 문자를 삽입 CSV형식으로 각 자료 사이에 ,를 넣을 수 있다
print("----------------------------------");
print(','.join(string));
print(','.format(string));
print('!!'.join(['a','b','c','d']));

#리스트 선언
print("----------------------------------");
scores = ['98','100','77','22','100'];#숫자로 하면 오류가 발생한다
print(','.join(scores));

#소문자를 대문자로 or 대문자를 소문자로 문자열.lower() 문자열.upper()
print("----------------------------------");
targetString = "abcdefg";
print(targetString.upper());
targetString = "ABcDEfG";
print(targetString.lower());

#공백제거
targetString = "    he ll o      "
print("----------------------------------");
print(targetString.lstrip());
print(targetString.rstrip());
print(targetString.strip());

#지정된 문자열을 새로운 문자열로 대체
#빈문자열 = empty string
print("----------------------------------");
print(targetString.replace(" ",""))
targetString = "Life is too short !!"
print(targetString.replace(" ",""))

#문자열 쪼개기 지정된 구분자(delimiter)를 기준으로 리스트로 반환한다
print("----------------------------------");
list = targetString.split()#공백이 길어도 쪼개진다
print(list[1]);
targetString = "Life,is,too,short,!!"
list = targetString.split(',')
print(list[3]);
print(list);
list = targetString.split(',',3)
print(list);
targetString = "A:      B:c:         D"
list = targetString.replace(" ","").split(':') #method chaining
print(list);
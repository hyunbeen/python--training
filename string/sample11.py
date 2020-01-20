#sample11.py
#f 문자열 예제
name = '홍길동'
age = 30
line = "나의 이름은 {0}입니다. 나이는 {1}입니다".format('남자'+name,age);

print(line);

print(f'나의 이름은 {name}입니다. 나이는 {age+10}입니다')

d={'name':'홍길동','age':30}

print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다')
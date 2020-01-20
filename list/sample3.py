#list/sample3.py

#리스트의 인덱싱과 슬라이싱

#인덱싱 : 이전의 문자열의 인덱싱과 동일하다
# 즉,리스트 변수명[인덱스번호] --> 인덱스번호에 해당하는 리스트의 요소를 참조(reference,사용)

l = [1,2,3]

element1 = l[0]
element2 = l[-1]
result = element1 + element2

print(l)

print("-------------------------------");


l = [1,2,3,
    
        [4,5,6,
        
            [7,8,9]
        
        ]

]

print(l[3][3][1]); #list의 8을 참조

l = [1,2,3,['a','b','c'],4,5]

list1 = l[3:4][0][2:3]
#list1 = l[3][2:3]
print(list1);
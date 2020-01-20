#sample10.py
while(not not []):
    print("-",end="")

#탈출조건과 코드를 가장 먼저 작성한다!!!

#전체요소의 값을 하나씩 가져다 사용하는 행위 --> 순회(Traverse)
list = {49:"3",10:"43",20:"25"}
for list1 in list : 
    print(list[list1]);
    pass

for (index,value)in enumerate(list) : 
    print(index);
    pass

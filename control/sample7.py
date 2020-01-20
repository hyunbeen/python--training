#sample7.py
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    
    if treeHit == 10:
        print("나무 넘어갑니다.")
        pass

print("-"*60)

number = 0;
prompt = '''

1.Add
2.Del
3.List
4.Quit

Enter number : '''
while(number!=4):
    try:
        number = int(input(prompt))
    except ValueError:
        print("값을 잘못 입력하셨습니다ㅇ")
    pass
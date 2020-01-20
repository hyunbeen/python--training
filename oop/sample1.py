#sample50.py

#caculaor :덧셈기능만 구현

def add (num1,num2):
    result = num1+num2
    return result

result =add(1,2)
reulst = add(result ,3)

#------------------------------------

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


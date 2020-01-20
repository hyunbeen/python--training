
from functools import reduce
import sys
sys.setrecursionlimit(100000)



def RecursionFactorial(n):   
    if(n<=2):
        return n
   
    return n*RecursionFactorial(n-1)


                                    
                

def IterationFactorial(n):
    answer = 1
    for i in range(2,n+1):
        answer *= i
    return answer

LambdaRecursionFactoral = lambda num: 1 if(num==1) else num*LambdaRecursionFactoral(num-1)



n = 4
ReduceFactorial = reduce(lambda x, y: x*y, [i for i in range(1,n+1)])

# result = list(map(lambda i: i * (i+1), [1,2,3,4]))
# print(result)


print(format(IterationFactorial(20),','));
print(RecursionFactorial(1000));
print(LambdaRecursionFactoral(4))
print(ReduceFactorial)



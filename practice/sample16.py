I = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
odd = lambda num : True if((num%2)!=0) else False 
print(list(filter(odd,I)))
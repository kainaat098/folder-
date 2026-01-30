from functools import reduce 
def sq():
    num = [1,2,3,4]
    result = reduce (lambda a,b : a*b , num)
    print(result)
sq()
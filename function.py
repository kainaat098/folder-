# def finish():
#     print("this code is completed and program run successfully")
    
    
    
# finish()    


# def table(x):
#     for a in range(10+1):
#         print(f"{x}X{a}={x*a}")
        
        
        
        
# table(23)  
# table(17)    # reusability  







def fibonacci (x):
    p2=0
    p1=1
    print(p2,p1,sep="   ",end="   ")
    for count in range(x-2):
        total=p2+p1
        print(total,end="   ")
        p2=p1
        p1=total
    print()
    #return total



nth=int(input("Enter The Position of fibo: "))
print(f"{nth} position: {fibonacci(nth)}")
#fibonacci(nth)   
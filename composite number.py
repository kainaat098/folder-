
# for n in range (2,22):
#     is_prime = True
#     for i in range (2,n):
#         # print(n,i)
#         if n % i == 0:
#             # print(i)
#             is_prime = False
#         continue
#     if not is_prime:
#         print(n)  
            

num = 2
while num < 22 :
    is_composite = False
    count = 2
    while count < num :
        if num % count == 0:
            # print(num,count)
            is_composite = True
            break
        count+=1
    if is_composite:
        print(num) 
    num+=1
    
    
    
    

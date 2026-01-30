# def loop (x):
#     if x>=10:
#         print(x)
#         return
#     print(x)
#     x+=1
#     loop(x)
# a=1
# loop(a)


# def loop (x):
#     if x<=1:
#         print(x)
#         return
#     print(x)
#     x-=1
#     loop(x)
# a=10
# loop(a)





# def loop(n,count,f):

#     if count>=n:
#         f*=count
#         print(f)
#         return
#     f*=count
#     count+=1
#     loop(n,count,f)

# f=1
# x=5
# count=1
# loop(x,count,f)
        
# p1=0
# p2=1
# print(p1)
# print(p2)
# for a in range (9):
#     p3=p1+p2
#     print(p3)
#     p1=p2
#     p2=p3





# def loop(p1,p2,a,nth):
    
#     print(p1)
#     p3=p1+p2
#     p1=p2
#     p2=p3
#     if a>=nth:   
#         return 
       
#     a+=1
#     loop(p1,p2,a,nth)
    
# p1=0
# p2=1
# a=1
# nth=9
# # print(p1)
# # print(p2)
# loop(p1,p2,a,nth)


# a=1
# while a < 10 :
#     print(a)
#     a+=1
#     if a == 5 :
#         break
    
# else:
#     print("loop runs successfully ")


for i in range (1,10):
    print(i)
    if i == 5:
        continue 
else :
    print("loop run successfully ")
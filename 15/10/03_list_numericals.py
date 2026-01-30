# Question no.1

# l=[1,2,3,4,5]
# a=0
# for i in l :
#     a+=i
# print(a)
 
# Question no.2

# l=[1,2,3,4,5]
# print(max(l))
# print(min(l))

# Question no.3

# l=[1,2,3,0,5]
# # l=[1,3,5]
# even = 0
# odd = 0
# for i in l :
#     if i==0:
#         continue
#     elif i % 2 == 0 :
#         even+=1
#         continue
#     odd+=1  
        
# print(f"There are {even} even numbers .")    
# print(f"There are {odd} odd numbers .")
    

# Question no.4 

# l=[1,2,3,4,5]
# for i in l :
#     print(i)

# Question no.5
# reverse the list without using .reverse()
# l=[1,2,3,4,5]
# print(l[::-1])
# Question no.6

# l=[1,2,3,4,5]
# a = len(l)
# total = 0
# for i in l :
#     total += i
# average = total / a
# print(average)


# Question no.8

# l=[1,2,3,4,5]
# l1=[]
# if l==l1:
#     print("list is empty")
# else:
#     print("list is not empty")
    
# Question no.8

# l=[1,2,3,4,5]
# l1 = l
# print(l1)

# Question no.9

# l=[1,2,3,4,5]
# x=4
# count=0
# is_absent=True
# length = len(l)

# while count <= length - 1:
#     if x==l[count]:
#         is_absent=False
#         print(f"{x} is on {count} index .")
#     count+=1
    
# if is_absent:
#     print("this value doesn't present in list .")
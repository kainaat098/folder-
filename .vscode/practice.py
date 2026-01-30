# num = "246"
# z=len(num)

# w=z-1
# num = int(num)
# x= num % 10
# y = num //10

# rotated_num = ((10**w)*x)+y
# print(rotated_num)


# num = int(input("Enter the number : "))
# r = num // 2
# temp = 0
# for a in range (1,r+1):
#     if num % a == 0:
#         print(f"a = {a}")
#         temp += a
#         print(f"temp= {temp}")
        
# if temp == num :
#     print("perfect number")
# else  :
#     print("not perfect number")
    

# num = input("Enter the number: ")
# numb = "3"
# print(num.count(numb))   
# print(num.count("3")) 
  

# num = input("Enter the number : ")
# count = 0
# a = "3"
# for i in num :
#     if i == a :
#         count +=1 
# print(count)


# num = input("Enter the number : ")
# n = len (num)
# is_greater = True
# for i in range (len(n)-1):
#     # print(int(num[i]))
#     # print(int(num[i]))

#     if int(num[i]) > (int(num[i+1])):
#         is_greater = False
#         break
# if is_greater :
#     print("YES") 

# num = "2345"
# n = len(num)
# a = 1
# if int(num) == 0:
    
#     print("Invalid input")
# else:

#     for i in num :

#         if int(i) == 0:
#             continue

#         elif int(i) % 2 == 0:
#             print(i)
#             a *= int(i)
    
# print(f"the product is {a}")

# num = "1123324455"
# n = ""
# for i in num :
#     if i not in n:
#         n+=i

# print(n) 




# num = "73942"
# n = len(num)
# a = int(num[0])

# for i in range (1,n):
#     if (a) < int(num[i]):
#         pass
#     else:
#         a = int(num[i])
        
# print(a)


num = "000"
n = len(num)

sum = 0
for i in range (n):
    sum += int(num[i])
print(f"sum after loop ended => {sum}")

productt = 1
for i in range (n):
    productt *= int(num[i])
print(f"productt after loop ended => {productt}")

if sum == productt :
    print("YES! it is a 'SPY-NUMBER'")
else :
    print("NO! it's not a 'SPY-NUMBER'")

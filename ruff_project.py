# x = input("Enter the operation you want : ")
# first_number,second_number = x
# print(first_number)
# print(second_number)
# if "+"=="+":
#     sum = first_number+second_number
#     print(sum)
    
    

# x=[1,2,3,4]
# a,b,c,d = x
# print(a,b,c,d)

x = input("Enter the operation you want : ").split("+")
first_number,second_number = x
print(first_number)
print(second_number)
print(type(first_number))
sum = float(first_number) + float(second_number)
# dict = {"+": sum }
print(sum)

# if x.split("+")== "+" :
#     print(sum)
    
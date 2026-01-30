# name=input("Enter your name: ")
# age=int(input("Enter your age : "))
# class_= int(input("Enter your class : "))
# roll_no=int(input("Enter your roll number : "))
# b = [name , age , class_ , roll_no]
# # b = [{name} , {age} , {class_} , {roll_no}]
# print(b) 
# print(type(b))


# input_data=["name","age","class","roll_no"]
 
# output_list=[]
# for i in input_data:
#     output_list.append(type(input(f"Enter your {i} : ")))
# print(output_list)


input_data= [input().split(),input().split(),input().split(),input().split()] 
input_data=[["name","str"],["age","int"],["class","int"],["roll_no","int"]]    
        
output_list=[]
for i in input_data:
    value=input(f"Enter your {i[0]} : ")
    if i[1]=="str":
       output_list.append(value)
    elif i[1]=="int":
       output_list.append(int(value))
    elif i[1]=="float":
       output_list.append(float(value))
    elif i[1]=="bool":
       output_list.append(bool(value)) 
print(output_list)
        


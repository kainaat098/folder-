dst={"name":"KK","age":22}
print(dst)
print(dst["name"])
# we can't find value using 'in' operator
print("KK"in dst)   
# but if we use key after dictionary
# print("KK"in dst["name"])  
for i in dst :
    print(i)
    print(dst[i])
    print(f"{i}:{dst[i]}")

# student={"name":"KK","Age":23,"smart":True}
# print(type(student["smart"]))
# student["smart"]=2.56
# print(type(student["smart"]))
# student["city"]="Nowgong"
# print(student)
# student.popitem()
# print(student)

# st={"name":"  "}
# print(st["name"])
# st={"name":None}
# print(st["name"])

# lst=[1,"",5,7,1,5,7,5,3,6,2,9,8]
# lst=(set(lst))
# # lst=list(set(lst))
# print(lst)
dict_1= {"name":"KK","age":23,"smart":True}
dict_1=(set(dict_1))
print(dict_1)
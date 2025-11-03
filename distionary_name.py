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


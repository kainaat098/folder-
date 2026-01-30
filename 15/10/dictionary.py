# data={"Name":"KK",
#       "Age": 23,
#     "city":"Bhopal"
#     }
# data["city"] = "Indore"
# data["gender"] = "Female"

# print(data)

# for i in data :
#     print(i)
# for i in data :
#     print(data[i])
# for i , j in data.items() :
#     print(i,j)

# .update() method
# data={"Name":"KK",
#       "Age": 23}

# data_2={"city":"Bhopal"}

# data.update(data_2)  
# print(data)  

# nested list 
student = {"101":{"Name":"KK","Age":23,"City":"Bombay"},
           "102":{"Name":"Lan zhan","Age":25,"City":"Shanghai"},
           "103":{"Name":"Wei","Age":27,"City":"Wuhan"}}

# print(student["102"])
# del student["101"]       # deletes key and whole dictionary
# print(student)

# student.pop("102")       # deletes only key (with value)
# print(student)

# student.popitem()          # deletes last inserted item
# print(student)

student.clear()
print(student)
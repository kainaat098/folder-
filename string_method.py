# # len function
# name = "My name is Khan"
# print(len(name))


# # .lower() method 
# print(name.lower())


# # .upper() method 
# print(name.upper())


# # .title() method
# print(name.title())


# # .count() method
# print(name.count("an"))
# print(name.count("na"))
# print(name.count("ie"))

# # strip method 
# name1 ="    Class     "
# dot="...."
# print(dot+name1+dot)

# # .lstrip()
# print(dot+name1.lstrip()+dot)

# # .rstrip()
# print(dot+name1.rstrip()+dot)

# # .strip()
# print(dot+name1.strip()+dot)


# # .replace()
# name_of_place = "Nowgong"
# print(name_of_place.replace ("gong","gaon"))

# # with count 
# '''
# replace (old , new , count)
# the counting starts with 0
# '''
# Str = "I am writing a novel whose name is Golden Freedom"
# print(Str.replace("o","ul"))
# Str = "I am writing a novel whose name is Golden Freedom"
# print(Str.replace("o","ul",2))


# # .find() this gives you postion 
# '''
# the counting starts with 0
# '''
# sTr = 'my name is kk and i want to do something new and "this is " is "".'
# print(sTr.find("is"))

# location = sTr.find("is")    # position = 8
# print(sTr.find("is",9))
# print(sTr.find("is",location + 1))

# center method 
name = "Kanak"
length = len (name)
print(name.center (length))
print(f"My name is {name.center (length)}")


name = "Kanak"
length = len (name)
print(name.center (length + 4))
print(f"My name is {name.center (length + 4)}")

name = "  Kanak"
length = len (name)
print(name.center (length + 8))
print(f"My name is {name.center (length + 8).strip()}.")

name = "  Kanak"
length = len (name)
print(name.center (length + 8))
print(f"My name is {name.strip().center (length + 8)} .")













# x={}
# print(type(x))
# x=()
# print(type(x))
# x=set()
# print(type(x))

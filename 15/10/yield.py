# # def gen():
# #     i = 1
# #     while i < 21:
# #         yield i
# #         i += 1
# # print(tuple(gen()))

# # enumerate 

# x = ["kk",20,20.7,"GOAT",False]
# for  i in enumerate (x): 
# # unpacking into count , i :
#     print( i)



x = input("enter the phone number : ")
if len (x) != 10 :
    raise NameError ("Phone number must have 10 digits.")
    # raise ValueError ("Phone number must have 10 digits.")
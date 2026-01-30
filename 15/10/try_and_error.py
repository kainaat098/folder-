

# try:
#     if 2 > 1:
#         print("hello")
# except SyntaxError :
#     print("syntax is wrong")
     
my_list = [ 2,"hello",8.90,True,None]
for i in my_list:
    try:
        print(int(i))
    except ValueError:
        print("Value error found" )
    except TypeError :
        print("Type error found")
    except:
        print("error occured")

from re import escape


a=0
while True :
    user_input=input("Enter the input : ").strip()
    
    try:
        user_input = int(user_input)
    except ValueError:
        pass  # Do nothing if it can't be converted

        
    
    if type(user_input) == int :
        a+=1
        
    elif type(user_input) == str and user_input =="exit" :
        print(a)
        break
    else :
        print("invalid input")
        print(a,"\n Try Again")   
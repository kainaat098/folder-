import random

welcome="""
**************Welcome to**************
**********'GUESS THE NUMBER'**********
*****************GAME*****************
"""
print(welcome)
def project (n,b):
    count = 0
    while count <= n :
        try:
            a = random.randint(0,b) 
            x = int(input("Enter the number : "))
            count+=1
            if (x < 0) or (x > b):
                print("Invalid input")
            elif a == x :
                print("You have guessed it correctly!")
                print("WINNER")
                print(f"You have taken {count} chances to guess it correctly! ")
                break
            else :
                print("You have guessed it wrong!")
        except Exception as e :
            print(f"An unexcepted error occured as :{e}")        
        
    print("Thank you for playing this game")

level = {
    "level 1" : ("Easy level",20,(9)),
    "level 2" : ("Medium level",15,(20)),
    "level 3" : ("Hard level",10,(50))
}
# print(level["level 1"][0])

print("choose a level")
print(
    """
    1 : ("Easy level",20 attemps,(0-9)numbers),
    2: ("Medium level",15 attemps,(0-20)numbers),
    3 : ("Hard level",10 attemps,(0-50)numbers)  
    """
) 
level_=input("Choose the level : ")
if level_ == "1":
    print(level["level 1"][0])
    print(project(level["level 1"][1],level["level 1"][2])) 

elif level_ == "2":
    print(level["level 2"][0])
    print(project(level["level 2"][1],level["level 2"][2])) 
    # print("level 2")
    # print(project(15,20)) 
elif level_ == "3": 
    print(level["level 3"][0])
    print(project(level["level 3"][1],level["level 3"][2])) 
    # print("level 3")  
    # print(project(10,50)) 
    
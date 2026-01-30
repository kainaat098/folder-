user_input = input("Enter the input : ")
n = 0
l = len(user_input)//2
is_pallendrom = False
for n in range(l) :

    if user_input[n] == user_input[-(n+1)]:
        is_pallendrom = True
        
    else :
        print("it's not a pallendrom")
        break
if is_pallendrom :
    print("it's a pallendrom")




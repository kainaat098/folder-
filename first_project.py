x = input("Enter the operation you want : ")


if "+" in x :
    first_number,second_number = x.split("+")
    sum = float(first_number) + float(second_number)
    print(f"{first_number} + {second_number} = {sum}")
    
elif "-" in x :
    first_number,second_number = x.split("+")
    difference = float(first_number) - float(second_number)
    print(f"{first_number} - {second_number} = {difference}")
          
elif "*" in x :
    first_number,second_number = x.split("+")
    multiplication = float(first_number) * float(second_number)
    print(f"{first_number} * {second_number} = {multiplication}")
elif "/" in x :
    first_number,second_number = x.split("/")
    
    if second_number != 0 :
        division = float(first_number) /float(second_number)
        print(f"{first_number} / {second_number} = {division}")
    else:
        print("ERROR, unrecognised operation ")

print("Program runs successfully . ")









        



   
    
   
   
     
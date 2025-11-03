name="naman"
count=0
is_pallendrom = False
for i in range(int(len(name)/2)):
    
    
    if name[count]==name[-(count+1)]:
        is_pallendrom=True

    else: 
        is_pallendrom=False
        print("it is not pallendrom")
        break
if is_pallendrom:
       print(("it is pallendrom"))
       
       
       
       
# name="naman"
# count=0
# for i in range(int(len(name)/2)):
#     # print(name[-(count+1)])
#     if name[count]==name[-(count+1)]:
#         print(("it is pallendrom"))
#     else:
#         print("it is not pallendrom")
    
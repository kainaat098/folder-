arra=[2,5,8,10,20,-1,-3,0]
odd=False
count=0
for i in arra:
    if i % 2 != 0:
        if count == 0:
            print("odd number found")
            odd=True
        count+=1
               
if not odd:
        print("no odd number found")
else:
    print(f"{count} odd numbers found")
        


# a=(2,3)
# b=(2,3)
# print(a is b)
lst=[1,3,2,5,6,9,20,50,100]
x=10
# isin=False
# for i in lst:         #range(len(lst)):
#     if i==x:
#         print("x is in list")
#         isin=True
#         break
# if not isin:
#     print("x is not in list")
is_present= x in lst
if is_present:
    print(f"{x} is present")
else:
    print(f"{x} is not present")       
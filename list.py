# numbers=[78,37,15,97]
# print(numbers[3])
# numbers=(78,37,15,97)
# numbers[3]=47      # #can't change value like list
# print(numbers[3])# numbers[3]=47


# l=[[True,1],["name",4.65],False,[]]

# print(["name",4.65][-1])
# l=[[True,1],["name",4.65],False,[]]
# for a in range (4):
#     print(l[a])
# l=[[True,1],["name",4.65],False,[]]
# for a in l:
#     print(a)


arra=[2,5,8,10,20,-1,-3,0]
odd=False
for i in arra:
    if i % 2 != 0:
        print("odd number found")
        odd=True
        break
if not odd:
    print("no odd number found")

    
    
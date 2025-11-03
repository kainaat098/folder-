l=[5,10,15,20,-5,-10,-15]
x=-10
is_in=False
for i in l:
    if i == x :
        print("variable found")
        is_in=True
        break
if not is_in:
    print("variable not found")
else:
    print(l.index(x))
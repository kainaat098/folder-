def even(x):
    check = x % 2 == 0
    return (check)

x = [1,2,3,4,5,6,7,8]
result = list (filter (even , x))
print (result)


def string_(x):
    check =  "k" in x
    return (check)

x = ["apple","kite","sap","kk"]
result = list (filter (string_ , x ))
print (result)
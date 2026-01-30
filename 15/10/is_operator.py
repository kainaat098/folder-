# a = {1,2,3}
# b = {"Apple","Banana","Grapes"}
# c = tuple(zip (a,b))
# print(c)

# a = [1,2,3]
# b = ["Apple","Banana","Grapes"]
# c = list(zip (a,b))
# print(c)


data = [(1,'Apple'), (2, 'Banana'), (3, 'Grapes')]
num,fruit = zip(*data)
print(num)
print(fruit)
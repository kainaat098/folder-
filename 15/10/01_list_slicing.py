# x=[1,2,3,[4,5,6,7],4,5,6]
# x=[8,5,6,9,2,7,3,1]
# x[3][2]=20      # list indexing
# x.reverse()
# print(x)

# for i in x :
#     print(i)

# l1=[1,2]
# l2=[3,4]
# # l1.extend(l2)
# # print(l1)
# l2.extend(l1)
# print(l2)
my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)



# def funct (ct , count):
#     if ct != 1:
#         if (ct % 2 == 0):
#             ct = ct // 2
#             print(ct)
#             count+=1
#             funct (ct , count)
#         else :
#             ct = (3 * ct )+ 1
#             print(ct)
#             count+=1
#             funct(ct , count)
#     else:
#         print(f"count is {count}")
#         return



# ct = int(input("A : "))
# count = 0
# funct(ct , count)



def func (*args):
    for i in args :
        print(i)
        
# func(1,2,3,4,5)
# func(1)
# func(1,5,6)
func(*(input("X : ").split (",")))

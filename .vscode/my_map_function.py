
def my_map (f,*args):
    try:
        result=[]
        for i in args :
            result.append(f(i))
        return result
    except:
        print("Unexpected Arguments")
        return
        
print(my_map((lambda x:x**2),1,2,3,4))
print(my_map((lambda x:x**2),[1,2,3,4]))
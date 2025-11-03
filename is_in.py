a=[1,"A"]
b=a
c=[1,"A"]
d=c

print(a is b)
print(b is a)
print(c is a)
b=d
print(c is b)

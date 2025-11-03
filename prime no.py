# is_prime=True
# n=13
# a=2
# while a<n:
#     if n % a==0:
#         print("this number is not prime")
#         is_prime=False
#         break
#     a+=1
# if is_prime:
#     print("this number is prime")


# for loop:

is_prime=True
n=23
for a in range(2,n):
    if n % a == 0:
        print("not a prime number")
        is_prime=False
        break
    a+=1
if is_prime:
    print("prime number")
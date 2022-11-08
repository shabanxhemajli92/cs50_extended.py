import pdb

minutes=int(input("How many minutes: "))
hours= minutes // 60
print(hours)

remainder= minutes - hours * 60
print(remainder)

x = int(input("first number: "))
y = int(input("second number: "))
if x % y == 0:
    print("x is / by y")
else:
    print("x is not/ by y")
pdb.set_trace()
x = int(input("first number: "))
y = int(input("second number: "))
if x % 2 ==0:
    print("num is even","+ it is also",True)
else:
    pdb.set_trace()    
    print("num is odd","+ it is also",False)
if 0 < x < 10:
        print('x is a positive single-digit number.')
else:
        print('x is a positive double-digit number.')
pdb.set_trace()
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)
print(countdown(8))    

a=[4,2,1,3]
a=a.sort()
b=None
print(a==b)
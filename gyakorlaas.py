import math

a=int(input("a "))
b=int(input("b "))

c=math.sqrt(a*a+b*b)

print("+c ",c)


#if c&1==0:
if c-c//1==0:
    print("egész")
else:
    print("nem egész")

for a in range(1,100):
    for b in range(1,100):
        c=math.sqrt(a*a+b*b)
        if c-c//1==0:
            print(a,b,c)


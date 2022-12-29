a=int(input("number 1: "))
b=int(input("number 2: "))
c=int(input("number 3: "))
d=int(input("number 4: "))


if a<b and a<c and a<d:
    smallest=a
    
elif b<a and b<c and b<d:
    smallest=b
    
elif c<a and c<b and c<d:
    smallest=c
    
else:
    smallest=d

print("The smallest number is:", smallest)

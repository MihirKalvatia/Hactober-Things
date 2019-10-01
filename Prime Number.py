#to prime number check
number=int(input("Enter a number: "))
c=0
for i in range(1,number+1):
    if number%i==0:
        c+=1
if c==2:
    print("Prime Number")
else:
    print("Not a Prime Number")

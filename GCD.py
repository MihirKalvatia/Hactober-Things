#to find Greatest Common Divisor of a two numbers

number1=int(input("Enter First Number: "))
number1=int(input("Enter Second Number: "))
maximum=max(number1,number2)

for i in range(1,maximum+1):
    if number1%i==0 and number2%i==0:
        z*=i
        number1=number1/i
        number2=number2/i
print("GCD:",z)

number1=float(input("Enter the first number:"))
number2=float(input("Enter the second number"))
total=0
print("The Operation in the Calculator are")
print("1.Addition (+)")
print("2.Subraction (-)")
print("3.Multipication (*)")
print("4.Division (/)")
print("5.Exit")
a=input("Enter your choice:")
if a=="+":
    total=number1+number2
    print("The sum of the numbers is:",total)
elif a=="-":
    total=number1+number2
    print("The subraction of the numbers is:",total)
elif a=="*":
    total=number1*number2
    print("The multipication of the numbers is:",total)
elif a=="/":
    total=number1/number2
    print("The divison of the numbers is:",total)
else:
    print("Invalid input")
        
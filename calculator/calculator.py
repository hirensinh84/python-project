no1=float(input("Enter first number: "))
no2=float(input("Enter second number: "))

print("Choose Operation:")
print("1.Addition\n2.subtraction\n3.multiplication\n4.division\n5.Remainder")
select=int(input("Enter your choice: "))

if select==1:
    print("Result",no1+no2)
elif select==2:
    print("Result",no1-no2)
elif select==3:
    print("Result",no1*no2)
elif select==4:
    print("Result",no1/no2)
elif select==5:
    print("Result",no1%no2)
else:
    print("Invalid choice")
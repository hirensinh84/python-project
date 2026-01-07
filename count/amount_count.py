amount=int(input("Enter any amount :"))

no=amount//500
print("500 note :",no)
amount=amount%500
no=amount//200
print("200 note :",no)
amount=amount%200
no=amount//100
print("100 note :",no)
amount=amount%100
no=amount//50
print("50 note :",no)
amount=amount%50
no=amount//20
print("20 note :",no)
amount=amount%20
no=amount//10
print("10 note :",no)
amount=amount%10
print("Extra :",amount)

import random as r

computer=r.randint(1,10)


count=0
while True:
    userno=int(input("Enter number: "))

    count+=1

    if 1>userno or 10<userno:
        print("Enter valid number betweeb 1 to 10")
    

    if userno==computer:
        print("Success : Correct Guess")
        break
    elif computer>userno:
        print("Your number was small. Take a big number")
    elif computer<userno:
        print("Your number was Big. Take a Small number")

    if count==5:
        print("-----------loss the game--------------")
        break
        

print("Your total Attempt:",count)
print("-------------Game Over-------------")    







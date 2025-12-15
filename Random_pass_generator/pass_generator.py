# Random Password Generator

import random
import string

allkey=f"{string.ascii_uppercase}{string.ascii_lowercase}{string.digits}{string.punctuation}"

password=""
lenno=int(input("Enter password length"))

for i in range(1,lenno+1):
    ran=random.choice(allkey)
    password+=ran


print(password)
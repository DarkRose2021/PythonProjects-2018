#Making a loop using while

import random
number = 0

while number !=7:
    print(number," ",end="")
    number = random.randint(1,20)
    
print("\n")

for i in range (20):
    if number !=7:
        print(number," ", end="")
    if number ==7:
        exit()
#Works just doesn't print the number

#Space Travel
#Katie King
print("A. Moon\nB. Mars\nC. Jupiter \nD. Alpha Centauri\nE. Saturn\n")

destination = input("What's choose your destination? ")
speed = int(input("What speed are you planning to travel at? (in miles per hours) "))

moon = round(((238900 / speed) / 8760),5)
mars = round(((33926867.096 / speed) / 8760) , 1)
jupiter = round(((365366261.036 / speed) / 8760) ,1)
ac = round(((15907537481110.335938 /speed) /8760) ,1)
sat = round(((745645430.6848 /speed) /8760) ,1)

if destination == "A":
    print("Going to the Moon at ",speed,"mph will take ",moon," years.")
    
if destination == "B":
    print("Going to Mars at ",speed,"mph will take ",mars," years.")

if destination == "C":
    print("Going to Jupiter at ",speed,"mph will take ",jupiter," years.")

if destination == "D":
    print("Going to Alpha Centauri at ",speed,"mph will take ",ac,"years.")

if destination == "E":
    print("Going to Saturn at ",speed,"mph will take ",sat," years.")

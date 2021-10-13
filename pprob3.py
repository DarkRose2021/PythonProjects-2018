#Calculate the area

print("We'll be calulating area.")

l = int(input("What should the length of a field be? Please use feet."))
w = int(input ("what should the width be? In feet."))
area = l * w
sqarea = round((area / 43560), 2)
print("The area (in square feet) of the field is ", sqarea ,".")


#Canadian pro football field
#330 feet long and 195 feet wide
le = 330
wi = 195
are = le * wi
print()
print("The area of the Canadian pro football field is ", are ,".")

#Pro soccer field
#15.9999 feet wide and 360 feet long
leg = 15.9999
wid = 360
ar = leg * wid
print()
print("The area of a pro soccer field is ", ar ,".")

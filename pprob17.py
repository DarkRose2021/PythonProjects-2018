#list
#Katie King
color = {"one": "blue", "two": "red", "three": "white", "four": "green", "five": "yellow", "six": "purple", "seven": "orange", "eight": "pink"}

for number, color in color.items():
    print("Number "+ number + " is "+ color)
print("\n")

for number in color.items():
    print(number)
print("\n")

for color in color.items():
    print(color)
print("\n")

for number, color in sorted(color.items()):
    print("Number "+ number + " is "+ color)
print("\n")

print(color)

print("\n")

response = input("Pick a number between one and eight ")

print(color[response])

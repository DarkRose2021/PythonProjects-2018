#BMI Problem
#Katie King
w = int(input("What's your weight in pounds? "))
h = int(input("What's your height in inches? "))

BMI = round((w * 720)/(h ** 2))

print("Your BMI is ", BMI,".")

print()

if (BMI == 18.5) or (BMI < 18.5):
    print("Your underweight")
elif(BMI > 18.5) and (BMI < 25):
    print("Your BMI is in the normal range")
elif(BMI == 25 or BMI > 25) and BMI < 30:
    print("Your overweight")
elif(BMI == 30 or BMI > 30) and BMI < 40:
    print("Your obese")
else:
    print("Your extremely obese")


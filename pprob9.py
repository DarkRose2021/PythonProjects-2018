#Wealth Builder
#Katie King
month = int(input("How much do you want to save per month? "))
print()
interest = float(input("What interest rate do you expect to earn? "))
print()
year = int(input("What year will you get that good job? "))
print()
retire = int(input("What year are you planning to retire? "))

savings = 0

oneyear =(month * 12)

workyears = retire - year

for i in range (workyears):
    savings = (savings + oneyear)
    savings = (savings + (savings * interest))



print("In one year you will have $",oneyear," saved up.")
print()
print("After ",workyears," years you would have $",round(savings)," saved up.")
print()
print("You will retire after ",workyears," years.")


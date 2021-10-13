#Funtions
#Katie King

again = "Y"

while again == "Y":

    print("\nA. Fahrenheit to Celsius to Fahrenheit\nB. Miles to Kilometers to Miles\nC. Teaspoon to Tablespoon to Cups\nD. Dollars to Euros to Dollars\nE. Litters to Gallons to Liters\n")

    chose = input("Chose one from above. ")

    print()

    if chose == "A":
        def main():
            f = 0
            c = 0
            print("Conversion of fahrenheit to celsius to fahrenheit.\n")
            f = int(input("What fahrenheit degree do you want to convert? "))
            print()
            convert(f)

        def convert(f):
            c = round(((f - 32) * 5 / 9) ,2)
            print(f," fahrenheit = ", c," celsius.\n")
            f = round(((c * 9 / 5) + 32) ,2)
            print(c," celsius = ",f," fahrenheit.\n")

        main()

    elif chose == "B":
        def main():
            m = 0
            k = 0
            print("Conversion of miles to kilometers to miles.\n")
            m = int(input("How many miles do you want to convert? "))
            print()
            convert(m)

        def convert(m):
            k = round((m * 1.609) ,2)
            print(m," miles = ", k," kilometers.\n")
            m = round((k / 1.609) ,2)
            print(k," kilometers = ",m," miles.\n")

        main()

    elif chose == "C":
        def main():
            te = 0
            ta = 0
            cu = 0
            print("Conversion of teaspoons to tablespoons to cups.\n")
            te = int(input("How many teaspoons do you want to convert? "))
            print()
            convert(te)

        def convert(te):
            ta = round((te / 3) ,2)
            print(te," teaspoons = ", ta," tablespoons.\n")
            cu = round((ta / 16.231) ,2)
            print(ta," tablespoons = ",cu," cups.\n")

        main()

    elif chose == "D":
        def main():
            d = 0
            e = 0
            print("Conversion of dollars to euros to dollars.\n")
            d = int(input("How many dollars do you want to convert? "))
            print()
            convert(d)

        def convert(d):
            e = round((d * 0.89) ,2)
            print(d," dollars = ", e," euros.\n")
            d = round((e * 1.13))
            print(e," euros = ",d," dollars.\n")

        main()

    elif chose == "E":
        def main():
            l = 0
            g = 0
            print("Conversion of liters to gallons to liters.\n")
            l = int(input("How many liters do you want to convert? "))
            print()
            convert(l)

        def convert(l):
            g = round((l / 3.785), 2)
            print(l," liters = ", g," gallons.\n")
            l = round((g * 3.785) ,2)
            print(g," gallons = ",l," liters.\n")

        main()

    again = input("Do you want to convert something again? ")

        

    


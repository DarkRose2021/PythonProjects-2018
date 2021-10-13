rainfall = [3.20, 3.31, 4.07, 3.60, 5.26, 4.44, 4.65, 3.25, 2.91, 3.13, 3.53, 3.93]

jan = rainfall[0]
feb = rainfall[1]
mar = rainfall[2]
apr = rainfall[3]
may = rainfall[4]
jun = rainfall[5]
jul = rainfall[6]
aug = rainfall[7]
sep = rainfall[8]
Oct = rainfall[9]
nov = rainfall[10]
dec = rainfall[11]


yearly = sum(rainfall)
print(yearly)
print()

monthly = print("Monthly Averages: \n\nJanuary = ",jan," \nFebuary = ",feb," \nMarch = ",mar," \nApril = ",apr," \nMay = ",may," \nJune = ",jun," \nJuly = ",jul," \nAugust = ",aug," \nSeptember = ",sep," \nOctober = ",Oct," \nNovember = ",nov," \nDecember = ",dec,"\n")

highest = max(rainfall)
print(highest)
print()

lowest = min(rainfall)
print(lowest)

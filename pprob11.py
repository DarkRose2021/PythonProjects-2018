#Mr.Bryn Ecology
#Katie King
pop = 1
time = 0

while pop < 70000:
    time += 20
    pop = (pop *2)
    #print("",time," the pop. will be",pop,"")
    
print("E. coli will reach 70,000 after ",int((time - 20)/60)," hours and ",((time - 20)%60)," minutes.")

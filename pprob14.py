#Ten Question Quiz
#Katie King
counter = 0

questions = ["Who was the first programmer? ", "What is Ada's full name (after she got married)?  ", "How did Ada program the first computer?  ", "What year did Ada make her program? ", "What was the type of numbers Ada used for her program? ", "What was the name of the software language the U.S. Department of Defense decticated to Ada Lovelace? ", "How old was Ada when she met Charles Babbage? ", "When is Ada Lovelace Day? ", "What did Ada excell at in school? ",  "What did Ada want to do when she was 12? "]
answer = ["A. Jean Bartik", "B. Frances Spence", "C. Ada Lovelace", "D. Grace Hopper" ,"A. Ada Lovelace", "B. Augusta Ada King Countess of Lovelace", "C. Augusta Ada Byron Countess of Lovelace", "D. Ada King Countess of Lovelace", "A. Punch cards", "B. Autocode", "C. LISP", "D. Regional Assembly Language", "A. 1843", "B. 1894", "C. 1952", "D. 1842", "A. Updown numbers", "B. Jacobi-Stirling numbers", "C. Zeta function", "D. Bernoulli numbers", "A. Lovelace", "B. Ada Lovelace", "C. Ada", "D. August", "A. 18", "B. 17", "C. 20", "D. 30", "A. 10/9/18", "B. Second Tuesday of October", "C. Second Tuesday of August", "D. Third Tuesaday of October", "A. English", "B. Programming", "C. Math", "D. Writing", "A. Fly", "B. Sing", "C. Program", "D. Learn another language"]

q1 = questions[0]
q2 = questions[1]
q3 = questions[2]
q4 = questions[3]
q5 = questions[4]
q6 = questions[5]
q7 = questions[6]
q8 = questions[7]
q9 = questions[8]
q10 = questions[9]

a1 = answer[0], answer[1], answer[2], answer[3]
a2 = answer[4], answer[5], answer[6], answer[7]
a3 = answer[8], answer[9], answer[10], answer[11]
a4 = answer[12], answer[13], answer[14], answer[15]
a5 = answer[16], answer[17], answer[18], answer[19]
a6 = answer[20], answer[21], answer[22], answer[23]
a7 = answer[24], answer[25], answer[26], answer[27]
a8 = answer[28], answer[29], answer[30], answer[31]
a9 = answer[32], answer[33], answer[34], answer[35]
a10 = answer[36], answer[37], answer[38], answer[39]

print(a1)
Answer = input(q1)

if Answer != "C":
    print("\nYou need to research more.\n")
else:
    print("\nGood Job!\n")
    counter += 10
    

print(a2)
Answer2 = input(q2)

if Answer2 != "B":
    print("\nYou need to research more.\n")
else:
    print("\nGood Job!\n")
    counter += 10
    

print(a3)
Answer3 = input(q3)

if Answer3 != "A":
    print("\nYou need to research more.\n")
else:
    print("\nGood Job!\n")
    counter += 10


print(a4)
Answer4 = input(q4)

if Answer4 != "A":
    print("\nYou need to research more.\n")
else:
    print("\nGood Job!\n")
    counter += 10


print(a5)
Answer5 = input(q5)

if Answer5 != "D":
    print("\nYou need to research more.\n")
else:
    print("\nGood Job!\n")
    counter += 10

print(a6)
Answer6 = input(q6)

if Answer6 != "C":
    print("\nYou need to research more.\n")
else:
    print("\nGood Job!\n")
    counter += 10


print(a7)
Answer7 = input(q7)

if Answer7 != "A":
    print("\nYou need to research more.\n")
else:
    print("\nGood Job!\n")
    counter += 10


print(a8)
Answer8 = input(q8)

if Answer8 != "B":
    print("\nYou need to research more.\n")
else:
    print("\nGood Job!\n")
    counter += 10


print(a9)
Answer9 = input(q9)

if Answer9 != "C":
    print("\nYou need to research more.\n")
else:
    print("\nGood Job!\n")
    counter += 10


print(a10)
Answer10 = input(q10)

if Answer10 != "A":
    print("\nYou need to research more.\n")
else:
    print("\nGood Job!\n")
    counter += 10

print("You made a(n) ",counter,".\n")


if counter >= 80:
    print("You passed!!!")
elif counter == 70:
    print("You barely passed.")
else:
    print("You failed")




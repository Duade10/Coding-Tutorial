def sc (list_): #Function that defines the instructions
    score = []   #Initialising the scores list
    for i in list_: #Iterates through all the instructions in the instructions list
        if i == "+":
            b = score[-1] + score[-2]
            score.append(b)
        elif i == "D":
            d = score[-1] * 2
            score.append(d)
        elif i == "C":
            score.pop()
        else:
            score.append(int(i))
    total = sum(score)
    print(total)
    return score

#Code to retrieve the instructions from the user
instructions = []
while True: #An infinite loop
    ins = input("Input the set of instructions, type end when you're done")
    if ins != "end": #Ensures that the loop stops when the user types end
        instructions.append(ins)
    else:
        break
   

sc(instructions)

import random 


def Number_1():
    print("The first question is ")
    score = 0
    a = random.randint(0,99)
    b = random.randint(0,99)
    Question = a + b
    answer= int(input(f"the answer in {a} + {b} is: "))
    if answer == Question:
        score += 1
    else:
        score += 0
    return score

def Number_2():
    print("The second question is ")
    score = 0
    a = random.randint(0,99)
    b = random.randint(0,99)
    Question = a + b
    answer= int(input(f"the answer in {a} + {b} is: "))
    if answer == Question:
        score += 1
    else:
        score += 0
    return score

def Number_3():
        print("The third question is ")
        score = 0
        a = random.randint(0,99)
        b = random.randint(0,99)
        Question = a + b
        answer= int(input(f"the answer in {a} + {b} is: "))
        if answer == Question:
            score += 1
        else:
            score += 0
        return score

def Number_4():
        print("The fourth question is ")
        score = 0
        a = random.randint(0,99)
        b = random.randint(0,99)
        Question = a + b
        answer= int(input(f"the answer in {a} + {b} is: "))
        if answer == Question:
            score += 1
        else:
            score += 0
        return score

def Number_5():
        print("The fifth question is ")
        score = 0
        a = random.randint(0,99)
        b = random.randint(0,99)
        Question = a + b
        answer= int(input(f"the answer in {a} + {b} is: "))
        if answer == Question:
            score += 1
        else:
            score += 0
        return score

def Number_6():
        print("The sixth question is ")
        score = 0
        a = random.randint(0,99)
        b = random.randint(0,99)
        Question = a + b
        answer= int(input(f"the answer in {a} + {b} is: "))
        if answer == Question:
            score += 1
        else:
            score += 0
        return score

def Number_7():
        print("The seventh question is ")
        score = 0
        a = random.randint(0,99)
        b = random.randint(0,99)
        Question = a + b
        answer= int(input(f"the answer in {a} + {b} is: "))
        if answer == Question:
            score += 1
        else:
            score += 0
        return score

def Number_8():
        print("The eighth question is ")
        score = 0
        a = random.randint(0,99)
        b = random.randint(0,99)
        Question = a + b
        answer= int(input(f"the answer in {a} + {b} is: "))
        if answer == Question:
            score += 1
        else:
            score += 0
        return score

def Number_9():
        print("The ninth question is ")
        score = 0
        a = random.randint(0,99)
        b = random.randint(0,99)
        Question = a + b
        answer= int(input(f"the answer in {a} + {b} is: "))
        if answer == Question:
            score += 1
        else:
            score += 0
        return score

def Number_10():
        print("The tenth question is ")
        score = 0
        a = random.randint(0,99)
        b = random.randint(0,99)
        Question = a + b
        answer= int(input(f"the answer in {a} + {b} is: "))
        if answer == Question:
            score += 1
        else:
            score += 0
        return score

def eval():
    if 5 <= Result == 10:
        print(f"Great Job",Name,"for completing the trainer")
    else:
        print(f"Better luck next time", Name, "Thank you!")

print("WELCOME TO THE ADDITION TRAINER!")
Name = input("First, what is your name?: ")

print(f"Hello", Name, ",We have 10 questions for you to answer. Goodluck!")

Result = int(Number_1() + Number_2() + Number_3()+ Number_4() + Number_5() + Number_6() + Number_7() + Number_8() + Number_9() + Number_10())

print(f"You got {Result} out of 10")
eval()

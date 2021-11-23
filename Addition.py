import random 

def Quiz_add():
    q1 = 1
    if q1 == 1:
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

print(Quiz_add())

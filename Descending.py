def arrange():
    Value_1 = int(input("Give a random number: "))
    Value_2 = int(input("Give a random number: "))
    Value_3 = int(input("Give a random number: "))
    Value_4 = int(input("Give a random number: "))
    if Value_1 > Value_2 and Value_1 > Value_3 and Value_1 > Value_4:
        if Value_2 > Value_3 and Value_3 > Value_4:
            print (f"The order of the number is {Value_1}, {Value_2}, {Value_3}, {Value_4}.")
        elif Value_2 > Value_3 and Value_2 > Value_4:
            print (f"The order of the number is {Value_1}, {Value_2}, {Value_4}, {Value_3}.")
        elif Value_2 < Value_3 and Value_2 > Value_4:
            print (f"The order of the number is {Value_1}, {Value_3}, {Value_2}, {Value_4}.")
        elif Value_2 < Value_3 and Value_3 > Value_4:
            print (f"The order of the number is {Value_1}, {Value_3}, {Value_4}, {Value_2}.")
        elif Value_2 < Value_3 and Value_3 < Value_4:
            print (f"The order of the number is {Value_1}, {Value_4}, {Value_3}, {Value_2}.")
        else:
            Value_2 > Value_3 and Value_2 < Value_4
            print (f"The order of the number is {Value_1}, {Value_4}, {Value_2}, {Value_3}.")
    elif Value_2 > Value_1 and Value_2 > Value_3 and Value_2 > Value_4:
        if Value_1 > Value_3 and Value_3 > Value_4:
            print (f"The order of the number is {Value_2}, {Value_1}, {Value_3}, {Value_4}.")
        elif Value_1 > Value_3 and Value_3 < Value_4:
            print (f"The order of the number is {Value_2}, {Value_1}, {Value_4}, {Value_3}.")
        elif Value_1 < Value_3 and Value_1 > Value_4:
            print (f"The order of the number is {Value_2}, {Value_3}, {Value_1}, {Value_4}.")
        elif Value_1 < Value_3 and Value_1 < Value_4:
            print (f"The order of the number is {Value_2}, {Value_3}, {Value_4}, {Value_1}.")
        elif Value_1 < Value_3 and Value_3 < Value_4:
            print (f"The order of the number is {Value_2}, {Value_4}, {Value_3}, {Value_1}.")
        else:
            Value_1 > Value_3 and Value_1 < Value_4
            print (f"The order of the number is {Value_2}, {Value_4}, {Value_1}, {Value_3}.")
    elif Value_3 > Value_1 and Value_3 > Value_2 and Value_3 > Value_4:
        if Value_1 > Value_2 and Value_2 > Value_4:
            print (f"The order of the number is {Value_3}, {Value_1}, {Value_2}, {Value_4}.")
        elif Value_1 > Value_2 and Value_1 > Value_4:
            print (f"The order of the number is {Value_3}, {Value_1}, {Value_4}, {Value_2}.")
        elif Value_1 < Value_2 and Value_1 > Value_4:
            print (f"The order of the number is {Value_3}, {Value_2}, {Value_1}, {Value_4}.")
        elif Value_1 < Value_2 and Value_2 > Value_4:
            print (f"The order of the number is {Value_3}, {Value_2}, {Value_4}, {Value_1}.")
        elif Value_1 > Value_2 and Value_1 < Value_4:
            print (f"The order of the number is {Value_3}, {Value_4}, {Value_1}, {Value_2}.")
        else:
            Value_1 < Value_2 and Value_2 < Value_4
            print (f"The order of the number is {Value_3}, {Value_4}, {Value_2}, {Value_1}.")
    else:
        Value_4 > Value_1 and Value_4 > Value_2 and Value_4 > Value_3
        if Value_1 > Value_2 and Value_2 > Value_3:
            print (f"The order of the number is {Value_4}, {Value_1}, {Value_2}, {Value_3}.")
        elif Value_1 > Value_2 and Value_1 > Value_3:
            print (f"The order of the number is {Value_4}, {Value_1}, {Value_3}, {Value_2}.")
        elif Value_1 < Value_2 and Value_1 > Value_3:
            print (f"The order of the number is {Value_4}, {Value_2}, {Value_1}, {Value_3}.")
        elif Value_1 < Value_2 and Value_2 > Value_3:
            print (f"The order of the number is {Value_4}, {Value_2}, {Value_3}, {Value_1}.")
        elif Value_1 > Value_2 and Value_1 < Value_3:
            print (f"The order of the number is {Value_4}, {Value_3}, {Value_1}, {Value_2}.")
        else:
            Value_1 < Value_2 and Value_2 < Value_3
            print (f"The order of the number is {Value_4}, {Value_3}, {Value_2}, {Value_1}.")

arrange()
def oneRepMax():
    keep_going = 0

    while keep_going == 0:
        oneRepMx = float(input("Enter your One Rep Max in Pounds: "))
        percent = float(input("Enter the percentage(ie 70% as .7) you would like to lift for this set: "))

        if oneRepMx >= 0 and percent >= 0 and percent <= 1:
            setWeight = oneRepMx * percent
            print(f"According to your {oneRepMx} and the lift percentage of {percent:.0%},")
            print(f"The weight you must lift for the set is {setWeight:,.0f} lb")
            keep_going = -1
        else:
            print("Invalid")

    # calculate the one rep max

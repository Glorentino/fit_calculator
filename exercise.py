from get_Weight_Lower import get_Weight_Lower
from get_Weight_Upper import get_Weight_Upper

# This Section is for one Rep Max Calculation if it is not known
def exercise():
    print("This calculator calculates the One Rep Max for Compound Exercises only.\n")
    exercise = input("Is the exercise targeted for Upper Body or Lower Body? Enter U or L")

    if exercise == "U" or exercise == "u":
        print("Great! So you would like to calculate an upper body exercise.")
        print("We can calculate your 1 Bench press max, 2 Incline Bench press, 3 Military/Shoulder press max, "
              "4 Rows max")
        upperBody = int(input("Enter a number according to the upper body exercise: "))

        if upperBody >= 1 and upperBody <= 4:
            if upperBody == 1:
                print("You selected Bench Press ")


            elif upperBody == 2:
                print("You selected Incline Bench Press")


            elif upperBody == 3:
                print("You selected Military/Shoulder press")


            elif upperBody == 4:
                print("You selected Bent Over Rows")
            get_Weight_Upper()
        else:
            print("Invalid! Try Again!")

    elif exercise == "L" or exercise == "l":
        print("Great! So you would like to calculate an lower body exercise.")
        print("We can calculate your 1 Squat max & 2 Deadlift press")

        lowerBody = int(input("Enter a number according to the lower body exercise: "))

        if lowerBody >= 1 and lowerBody <= 2:
            if lowerBody == 1:
                print("You selected Squat")


            elif lowerBody == 2:
                print("You selected Deadlift")
            get_Weight_Lower()

        else:
            print("Invalid! Try Again")

    # Users picks the exercise
    # The number = exercise so that user does not need to type  and make sure that
    # if it's not in the range to ask again




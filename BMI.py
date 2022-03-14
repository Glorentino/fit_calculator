def BMI():
    # BMI = (weight in pounds x 703) / (height in inches x height in inches)
    print("Welcome to the BMI calculator!\n")
    keep_going = 0
    while keep_going == 0:
        weight = float(input("Enter How much you weigh in pounds(lb):"))
        height = float(input("Enter how tall you are in inches(in):"))

        if weight> 0 and weight > 0:
            bmi = (weight * 703)/ height**2
            print(f"According to your height of {height} in and weight of {weight} lbs,")
            print(f"Your BMI is {bmi:,.1f}.")
            if bmi <= 18.5:
                print("According to BMI, You fall in the Underweight category")
            elif bmi >= 18.6 and bmi <= 24.9:
                print("According to BMI, You fall in the Normal Weight category")
            elif bmi >= 25.0 and bmi <= 29.9:
                print("According to BMI, You fall in the Overweight category")
            elif bmi >= 30.0 and bmi <= 34.9:
                print("According to BMI, You fall in the Obese category")
            elif bmi >= 35.0:
                print("According to BMI, You fall in the Extremely Obese category")
            keep_going = -1
        else:
            print("Reenter height and weight again.")

    # user receives BMI by inputing their weight in lb and height in inches.
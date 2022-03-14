from exercise import exercise
from oneRepMax import oneRepMax
from BMI import BMI

def main():
    print("Welcome to Chris's Fitness Calculator!\n")
    cont = input("Would you like to continue? Enter Y or N")

    if cont == "Y" or cont == "y":
        while cont == "Y" or cont == "y":
            user = int(input("Enter 1 for One Rep Max Calculator, 2 for Lift percentage or 3 for BMI calculation: "))
            if user == 1:
                exercise()
            elif user == 2:
                oneRepMax()
            elif user == 3:
                BMI()
            cont = input("Would you like to calculate something else? Y or N")
            if cont == "N" or "n":
                print("Thank you! See you soon!")

    else:
        print("Thank you! See you soon!")

main()

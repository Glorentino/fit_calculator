def get_Weight_Lower():
    # (4-to-6RM x 1.09703) + 14.2546
    kgConversion = 2.2
    print("Lower: We must find out how much weight you can lift at a 4-6 RPM ")
    keep_going = 0

    while keep_going == 0:
        weight = float(input("Enter How much you you lift in pounds: "))
        if weight >= 0:
            oneRepMax = (((weight / kgConversion) * 1.09703) + 14.2546) * kgConversion
            print(f"Your One rep max is {oneRepMax:,.2f} ~ {oneRepMax:,.0f} lb")
            keep_going = -1
        else:
            print("Invalid! Reenter the amount again!")
# This function calculates lower body one rep max. Has a while loop just in case they enter -1 and makes user renter
# a valid entry
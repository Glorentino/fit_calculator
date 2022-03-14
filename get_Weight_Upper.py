def get_Weight_Upper():
    # (KG x 1.1307) + 0.6998
    kgConversion = 2.2
    print("Upper: We must find out how much weight can you lift at a 4-6 RPM")
    keep_going = 0

    while keep_going == 0:
        weight = float(input("Enter How much can you lift in pounds: "))
        if weight >= 0:
            oneRepMax = (((weight / kgConversion) * 1.1307) + 0.6998) * kgConversion
            print(f"Your One rep max is {oneRepMax:,.2f} ~ {oneRepMax:,.0f} lb")
            keep_going = -1
        else:
            print("Invalid! Reenter the amount again!")
# This function calculates upper body one rep max. Has a while loop just in case they enter -1 and makes user renter
# a valid entry
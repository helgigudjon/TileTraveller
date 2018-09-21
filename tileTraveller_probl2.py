def att(a):
    if a == 1.1:
        attin = "(N)orth."
    if a == 1.2:
        attin = "(N)orth or (E)ast or (S)outh."
    if a == 1.3:
        attin = "(E)ast or (S)outh."
    if a == 2.1:
        attin = "(N)orth."
    if a == 2.2:
        attin = "(S)outh or (W)est."
    if a == 2.3:
        attin = "(E)ast or (W)est."
    if a == 3.1:
        attin = "(N)orth."
    if a == 3.2:
        attin = "(N)orth or (S)outh."
    if a == 3.3:
        attin = "(S)outh or (W)est."
    return attin

position = 1.1
villa = 0
while position != 3.1:
    if villa == 1:
        direction = input("Direction: ").lower()
        villa = villa - 1
    else:
        print("You can travel:", att(position))
        direction = input("Direction: ").lower()
    if direction == "n":
        if position == 1.1 or position == 1.2 or position == 3.2 or position == 2.1:
            position = position + 0.1
        else:
            print("Not a valid direction!")
            villa = villa + 1
    elif direction == "s":
        if  position == 1.2 or position == 1.3 or position == 2.2 or position == 3.3 or position == 3.2:
            position = position - 0.1
        else:
            print("Not a valid direction!")
            villa = villa + 1
    elif direction == "w":
        if position == 2.3 or position == 2.2 or position == 3.3:
            position = position - 1
        else:
            print("Not a valid direction!")
            villa = villa + 1
    elif direction == "e":
        if position == 1.2 or position == 1.3 or position == 2.3:
            position = position + 1
        else:
            print("Not a valid direction!")
            villa = villa + 1
    else:
        print("Not a valid direction!")
        villa = villa + 1
    position = round(position, 1)
print("Victory!")


#GitHub -->     https://github.com/helgigudjon/TileTraveller.git

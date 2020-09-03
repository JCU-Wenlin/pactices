"""
CP1404/CP5632 - Practical
Broken program to determine score status
    """


# TODO: Fix this!
def main():
    sco = float(input("Enter score: "))
    while sco == sco:
        if sco < 0:
            print("Invalid score")
            sco = float(input("Enter score: "))
        elif sco > 100:
            print("Invalid score")
            sco = float(input("Enter score: "))
        elif 90 > sco >= 50:
            print("Passable")
            sco = float(input("Enter score: "))
        elif 100 >= sco >= 90:
            print("Excellent")
            sco = float(input("Enter score: "))
        else:
            print("Bad")
            sco = float(input("Enter score: "))


main()

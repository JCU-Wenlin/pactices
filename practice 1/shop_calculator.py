def main():
    item = int(input("How many item? "))
    total = 0
    while item == 0:
        print("Invalid number of items!")
        item = int(input("How many item?"))
    for i in range(item):
        total += float(input("Price of item: $"))
    if total > 100:
        final = total * 0.9
        print("Total price for  " + str(item) + " items is $ " + str(final))
    else:
        print("Total price for " + str(item) + " items is $" + str(total))


main()

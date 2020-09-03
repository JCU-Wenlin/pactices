def main():
    for one in range(1, 21, 2):
        print(one, end=' ')
    print()


main()


def main2():
    for two in range(0, 110, 10):
        print(two, end=' ')
    print()


main2()


def main3():
    for three in range(20, 0, -1):
        print(three, end=' ')
    print()


main3()


def main4():
    stars = int(input("How many stars do you want?"))
    print("Number of stars:" + str(stars))
    for four in range(stars):
        print("*", end=' ')


main4()


def main5():
    print()
    star = int(input("How many stars do you want?"))
    for i in range(star):
        print("*" * (i + 1))


main5()

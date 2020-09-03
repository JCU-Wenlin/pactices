"""
import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

What did you see on line 1?
5~19, all integers
What was the smallest number you could have seen, what was the largest?
Smallest is 5,largest is 19
What did you see on line 2?
3,5,7,9
What was the smallest number you could have seen, what was the largest?
Smallest is 3,largest is 9
Could line 2 have produced a 4?
No
What did you see on line 3?
2.500000000000000>= number > 5.500000000000000
What was the smallest number you could have seen, what was the largest?
Smallest is 2.500000000000000,largest is 5.499999999999999
"""
import random


def main():
    print(random.uniform(0, 101))


main()

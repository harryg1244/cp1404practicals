"""
What did you see on line 1?
    What was the smallest number you could have seen, what was the largest?
        The smallest number is 5, and the largest is 20.

What did you see on line 2?
    What was the smallest number you could have seen, what was the largest?
        The smallest number is 3, and the largest is 9

    Could line 2 have produced a 4?
        No, it can only produce odd numbers. Starting at 3 and ranging to 10, having additions of 2 starting from 3 to find the random numbers. (3, 5, 7, 9)

What did you see on line 3?
    What was the smallest number you could have seen, what was the largest?
        The smallest number is 2.5, and the largest is 5.5.
"""

#Write code, not a comment, to produce a random number between 1 and 100 inclusive.
import random
print(random.randint(1, 100))
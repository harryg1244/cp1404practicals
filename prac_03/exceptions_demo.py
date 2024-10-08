"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    If the input is not a valid number. e.g. letter (abc), 6.66, four

2. When will a ZeroDivisionError occur?
    If the input for the denominator is zero. Numbers and Zero cannot be divided by  zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, by adding some code along the lines of:
    if denominator == 0
    print("Cannot divide by zero!")
    Since we are now checking for 0, the error exception doesn't display.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
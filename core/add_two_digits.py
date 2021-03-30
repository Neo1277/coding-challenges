"""
You are given a two-digit integer n. Return the sum of its digits.

Example

For n = 29, the output should be
addTwoDigits(n) = 11.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] integer n

    A positive two-digit integer.

    Guaranteed constraints:
    10 ≤ n ≤ 99.

    [output] integer

    The sum of the first and second digits of the input number.

"""


def addTwoDigits(n):
    if n > 0:
        n = str(n)
        summ = (int(n[0]) + int(n[1]))
    return summ
"""
This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
"""
def simple_multiplication(number) :
    if number % 2 == 0:
        return int(number) * 8
    else:
        return int(number) * 9
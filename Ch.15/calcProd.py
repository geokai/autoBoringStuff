"""This script calculates the product of the first 100,000 numbers.
The result is returned and the number of digits of the resulting number
are given by the 'len(str())' methods.
The time taken for both the calculation and the counting are given.
"""

import time

def calc_prod():
    """Calculate the product of the first 100,000 numbers."""
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

SPC = 60

print()
print('–' * SPC)
print()
print('Calculating the product of the first 100,000 numbers...')
print()
print('–' * SPC)
print()
print('Starting calculation...')
startTime = time.time()
prod = calc_prod()
endTime = time.time()
print('...finished calculation.')

print('Starting counting...')
startTime2 = time.time()
num_digits = (len(str(prod)))
endTime2 = time.time()
print('...finished counting.')
print()
print('The result is a number, %s digits long.' % num_digits)
print()

print('It took %s seconds to calculate the number,' % (endTime - startTime))
print('and %s seconds to count the digits.' % (endTime2 - startTime2))
print()
print('–' * SPC)
print()

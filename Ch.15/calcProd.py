import time

def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()

startTime2 = time.time()
print('The result is %s digits long.' % (len(str(prod))))
endTime2 = time.time()

print('Took %s seconds to calculate,' % (endTime - startTime))
print('and %s seconds to count the digits.' % (endTime2 - startTime2))

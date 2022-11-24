
import math


# Multiply all the items of a List

numbers = [3,4,5,6]
product = math.prod(numbers)
print(product)
#output: 360


# Multiply with start argument in Tuples

numbers = (3,4,5,6)
product = math.prod(numbers, start =2)
print(product)
#output: 720 , multilplies by 2


# Multiply with Range function

numbers = range(5,11)
product = math.prod(numbers)
print(product)
#output: 151200

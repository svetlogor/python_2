from python_2_2 import sum_numbers
from random import randint

numbers_generation = [randint(0, 100) for i in range(randint(0, 100))]
print(numbers_generation)
print(sum_numbers(numbers_generation))
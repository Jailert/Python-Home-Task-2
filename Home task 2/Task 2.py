# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

import math

Number = int(input('Enter Number '))
MultiplyList = []

for i in range(1, Number+1):
    MultiplyList.append(math.factorial(i))
print(MultiplyList)

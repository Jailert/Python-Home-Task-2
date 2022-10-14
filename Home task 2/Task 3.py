# Задайте список из n чисел последовательности
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.

number = int(input('Enter Number '))
mylist = {}
sum = 0

for i in range(1, number + 1):
    mylist[i] = (1 + 1/i)**i
    sum += mylist[i]
print(f' List : {mylist}')
print(f' Sum = {sum}')

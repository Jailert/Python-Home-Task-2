# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.


number = input('Enter number: ')

if '.' in number:
    splitnumber = number.split(".")

    whole = int(splitnumber[0])
    fractional = int(splitnumber[1])

    sum = 0

    while (whole != 0):
        sum = sum + (whole % 10)
        whole = whole // 10

    while (fractional != 0):
        sum = sum + (fractional % 10)
        fractional = fractional // 10
else:
    number = int(number)
    sum = 0
    while number > 0:
        sum = sum + (number % 10)
        number = number // 10
print(sum)

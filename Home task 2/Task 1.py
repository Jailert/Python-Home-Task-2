# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

number = input('Enter number: ')


def digitsum(n):
    sum = 0
    while n != 0:
        sum = sum + (n % 10)
        n = n // 10
    return sum


if '.' in number:
    splitnumber = number.split(".")

    whole = int(splitnumber[0])
    fractional = int(splitnumber[1])
    print(f' Sum :{(digitsum(whole) + digitsum(fractional))}')
else:
    number = int(number)
    print(f' Sum : {digitsum(number)}')

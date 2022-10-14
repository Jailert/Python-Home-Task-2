# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


def fillfile(b):
    lst = []
    for i in range(-b, b+1):
        lst.append(i)
    else:
        return lst


n = int(input('Enter N '))

with open('Task 4.txt', mode='w+') as my_file:
    for i in range(0, n*2+1):
        my_file.write(str(f'{fillfile(n)[i]}\n'))

with open('Task 4.txt', mode='r+') as my_file:
    multiply = my_file.read()
    multiply = multiply.split('\n')
    multiply.remove('')

    for i in range(1, n*2+2):
        x = int(multiply[i-1])*i
        print(f'Line {i} X {str(multiply[i-1])} = {x}')

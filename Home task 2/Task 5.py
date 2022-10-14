# Реализуйте алгоритм перемешивания списка.

from datetime import datetime
import random

listrange = int(input('Enter list range: '))

mylist = []

for i in range(1, listrange):
    mylist.append(random.randint(-10, 10))
print(f'Initial list: {mylist}')

a = len(mylist)
changedlsit = [0 for i in range(a)]

now = datetime.now()
now = str(now)
now = now.split('.')
now = now[1]
kindarandom = int(now) % a

for i in range(a):
    x = i - kindarandom
    changedlsit[i] = (mylist[x])


print(f' Changed list : {changedlsit}')

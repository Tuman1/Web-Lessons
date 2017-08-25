'''Генерировать случайный массив из чисел 1-100.
Написать функцию, которая найдет пару чисел с фиксированной суммой.
Вход - массив и необходимую сумму
Возврат - пара чисел'''

import random
arrayRand = [random.randrange(1, 100) for x in range(0, 100)]

# arrayRand = [4, 7, 3, 11, 8, 3, 2, 6, 1, 0, 8]
sum = 17

# print(arrayRand)

def FindSum(array, sum):
    array.sort() # эту строчку я заменю, после того как реализую алгоритм сортировки слиянием.
    leftBord = 0;
    rightBord = len(array) - 1;
    for i in range(len(array)):
        if ( array[leftBord] + array[rightBord] > sum):
            rightBord -= 1
        elif ( array[leftBord] + array[rightBord] < sum ):
            leftBord += 1
        elif (array[leftBord] + array[rightBord] == sum):
            return leftBord, array[leftBord], rightBord, array[rightBord]
        else:
            print("There are no numbers for sum = {}".format(sum))
            return None

print(FindSum(arrayRand, sum))

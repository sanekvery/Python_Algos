"""
Задание_1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

Подсказка: используйте вложенный цикл

Пример:
В диапазоне 2-99: 49 чисел кратны 2
В диапазоне 2-99: 33 чисел кратны 3
В диапазоне 2-99: 24 чисел кратны 4
В диапазоне 2-99: 19 чисел кратны 5
В диапазоне 2-99: 16 чисел кратны 6
В диапазоне 2-99: 14 чисел кратны 7
В диапазоне 2-99: 12 чисел кратны 8
В диапазоне 2-99: 11 чисел кратны 9





def devuser(n):
    usernum = n
    counter = 0
    for i in range(2,100):
        if i % usernum == 0:
            counter += 1
        if i >= 99:
            print(f'В диапазоне 2-99: {counter} чисел кратны {n}')


devuser(2)
devuser(3)
devuser(4)
devuser(5)
devuser(6)
devuser(7)
devuser(8)
devuser(9)

"""


usernum1 = 2
counter1 = 0
for i in range(usernum1, 10):
    for u in range(2,100):
        if u % i == 0:
            counter1 += 1
        if u >= 99:
            print(f'В диапазоне 2-99: {counter1} чисел кратны {i}')
            counter1 = 0

Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, 
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и 
той же стороной. Выведите минимальное количество монет, 
которые нужно перевернуть

n = int(input("Введите количество монеток: "))
reshka_count = 0
gerb_count = 0

for i in range(n):
    side = int(input(f"Введите сторону монетки (0 - решка, 1 - герб): "))
    if side == 0:
        reshka_count += 1
    else:
        gerb_count += 1

min_coins = min(reshka_count, gerb_count)
print(f"Минимальное количество монет, которые нужно перевернуть: {min_coins}")

Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа
X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и
их произведение P.                           
Помогите Кате отгадать задуманные Петей числа.


s = int(input('Задай сумму двух чисел: '))
p = int(input('Задай произведение чисел: '))
 
found_numbers = False
 
for x in range(1, s):
    for y in range(1, s):
        if s == x + y and p == x * y:
            print(f'Первое число: {x}, второе число: {y}')
            found_numbers = True
 
if not found_numbers:
    print('Числа X и Y не удалось найти.')

Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
не превосходящие числа N.

N = int(input("Введите число N: "))

k = 1
degree_of_two = 2

while degree_of_two <= N:
    print(degree_of_two)
    k += 1
    degree_of_two = 2 ** k
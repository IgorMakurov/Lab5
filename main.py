#Задана рекуррентная функция. Область определения функции – натуральные числа.
#Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
#Определить границы применимости рекурсивного и итерационного подхода.
#Результаты сравнительного исследования времени вычисления представить в табличной форме.
#Обязательное требование – минимизация времени выполнения и объема памяти.
#Вариант 13
#F(1) = 1, F(n) = (-1)n*(F(n–1)+ (n - 2)! /(2n)!), при n > 1

import time
import math
from decimal import Decimal
import sys

# Увеличивает глубину рекурсии
sys.setrecursionlimit(10000)

#Вычисление факториалов
def factorial(n, prev_fact = 1, prev_n = 0):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == prev_n + 1:
       return prev_fact * n
    return factorial(n - 1) * n

#Рекурсивное вычисление
def recursive_F(n, prev_F = Decimal(1), prev_fact = Decimal(1), prev_n = 1):
    if n == 1:
        return Decimal(1)
    
    prev_fact = factorial(n-2, prev_fact, prev_n-2) if n > 2 else 1

    result = ((-1)**n) * (prev_F + (Decimal(prev_fact) / Decimal(factorial(2 * n, 1, 0))))

    return recursive_F(n - 1, result, factorial(n-2, prev_fact, n-2) if n > 2 else 1, n-1)

#Итерационное вычисление
def iterative_F(n):
    if n == 1:
        return Decimal(1)
    
    prev_F = Decimal(1)
    prev_fact = Decimal(1)

    for i in range(2, n + 1):
        prev_fact =  prev_fact * (i-2) if (i - 2) > 0 else 1
        result = ((-1)**i) * (prev_F + (Decimal(prev_fact) / Decimal(factorial(2 * i, 1, 0))))
        prev_F = result

    return result
        

#Сравнение и вывод
def compare_methods(max_n):
    print("{:<5} {:<15} {:<15} {:<15} {:<15}".format("n", "Рекурсия (сек)", "Итерация (сек)", "Разница (сек)", "Разница (%)"))
    print("-" * 65)
    for n in range(1, max_n + 1):
        start_time = time.time()
        recursive_result = recursive_F(n)
        recursive_time = time.time() - start_time

        start_time = time.time()
        iterative_result = iterative_F(n)
        iterative_time = time.time() - start_time

        time_diff = recursive_time - iterative_time
        percentage_diff = (time_diff / recursive_time) * 100 if recursive_time != 0 else 0

        print("{:<5} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.2f}".format(n, recursive_time, iterative_time, time_diff, percentage_diff))

while True:
    try:
        max_n = int(input("Введите максимальное значение n (целое положительное число): "))
        if max_n <= 0:
            print("Пожалуйста, введите положительное целое число.")
        else:
            break
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")
compare_methods(max_n)

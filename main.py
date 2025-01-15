#Задана рекуррентная функция. Область определения функции – натуральные числа.
#Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
#Определить границы применимости рекурсивного и итерационного подхода.
#Результаты сравнительного исследования времени вычисления представить в табличной форме.
#Обязательное требование – минимизация времени выполнения и объема памяти.
#Вариант 13
#F(1) = 1, F(n) = (-1)n*(F(n–1)+ (n - 2)! /(2n)!), при n > 1

import time
from math import factorial
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial_cache(n):
  return factorial(n)


def f_recursive_lru(n):
    if n == 1:
        return 1
    return (-1) ** n * (f_recursive_lru(n - 1) + factorial_cache(n-2) / factorial_cache(2*n))




def f_iterative(n):
    if n == 1:
        return 1
    result = 1
    prev_result = 1
    fact_n_minus_2 = 1
    fact_2n = 1
    for i in range(2, n + 1):
        
        fact_n_minus_2 *= (i - 2)
        
        for j in range (2 * (i-1) + 1, 2 * i + 1 ):
            fact_2n *= j
        result = - (prev_result + fact_n_minus_2 / fact_2n)
        prev_result = result   
    return result


def compare_functions(n):
    print(f"{'n':<5} {'Recursive (ms)':<25}  {'Iterative (ms)':<15}")
    print("-" * 50)
    for i in range(1, n + 1):
        start_time = time.perf_counter()
        f_recursive_lru(i)
        recursive_lru_time = (time.perf_counter() - start_time) * 1000
        start_time = time.perf_counter()
        f_iterative(i)
        iterative_time = (time.perf_counter() - start_time) * 1000
        print(f"{i:<5} {recursive_lru_time:<25.5f} {iterative_time:<15.5f}")


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Введите натуральное число n: "))
            if n <= 0:
                print("Пожалуйста, введите натуральное число (больше 0).")
            else:
                break
        except ValueError:
            print("Ошибка: введите целое число.")
    compare_functions(n)
    print("Выполнение программы завершено.")

from time import time


def factorial_func(num: int) -> int:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


def factorial_generator(num: int) -> int:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    yield factorial


def factorial_recursive(num):
    if num == 0:
        return 1
    else:
        return num * factorial_recursive(num - 1)


num_for_calc = int(input("Введите число: "))

results = {}
start_time1 = time()
result1 = factorial_func(num_for_calc)
end_time1 = time()
elapsed_time1 = end_time1 - start_time1
results["Обычная функция"] = elapsed_time1

print(f"Факториал {num_for_calc} равен {result1}",
      f"Время работы обычной функции факториала: {elapsed_time1} секунд",
      sep="\n"
      )

start_time2 = time()
result2 = next(factorial_generator(num_for_calc))
end_time2 = time()
elapsed_time2 = end_time2 - start_time2
results["Генератор"] = elapsed_time2

print(f"Время работы генератора по вычислению факториала: {elapsed_time2} секунд",
      sep="\n"
      )

start_time3 = time()
result3 = factorial_recursive(num_for_calc)
end_time3 = time()
elapsed_time3 = end_time3 - start_time3
results["Рекурсивная функция"] = elapsed_time3
print(f"Время работы рекурсивной функции по вычислению факториала: {elapsed_time3} секунд",
      sep="\n"
      )

best_func = 0
for key, value in results.items():
    if value == min(results.values()):
        best_func = key
print(f"Наиболее быстрый метод вычисления факториала - {best_func}")

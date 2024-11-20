# Задание 1

a, b = int(input("Введите A: ")), int(input("Введите B: "))
summ1 = 0
for i in range(a, b + 1):
    summ1 += i
print("Cумма всех целых чисел в интервале [A; B] =", summ1)

# Задание 2

summ2 = 0
if a >= 1 and b >= 1:
    for i in range(a, b + 1):
        summ2 += i
elif a < 0 and b >= 1:
    for i in range(1, b + 1):
        summ2 += i
print("Cумма всех натуральных чисел в интервале [A; B] =", summ2)

# # Задание 3

summ3 = 0
multip3 = 1
negative_counter = 0
for i in range (1, 11):
    num = int(input(f"Введите число № {i}: "))
    if num > 0:
        multip3 *= num
    elif num < 0:
        summ3 += num
        negative_counter += 1
print(f"Произведение положительных чисел = {multip3}",
      f"Cумма отрицательных чисел = {summ3}",
      f"Количество отрицательных чисел = {negative_counter}", sep="\n"
      )

# Задание 4

swimmers_results = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17
}

best_result_value = min(swimmers_results.values())
best_swimmer = 0
for i in swimmers_results.keys():
    if swimmers_results[i] == best_result_value:
        best_swimmer = i
        break
print(f"Лучший результат заплыва показал пловец {best_swimmer} - {best_result_value}")

# Задание 5

arr = [1, 5, 2, 9, 2, 9, 1]
unique_number = 0
for i in arr:
    if arr.count(i) == 1:
        unique_number = i
print("Уникальное число в массиве:", unique_number)




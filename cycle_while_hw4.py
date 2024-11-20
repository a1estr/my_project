# Задание 1

n1 = int(input("Введите число N: "))
if n1 > 0:
    i = 1
    multip1 = 1
    while i <= n1:
        multip1 *= i
        i += 1
    print(f"Произведение чисел равно {multip1}")
if n1 == 0:
    print("Произведение чисел равно нулю")

# Задание 2

s1, s2 = int(input("Введите площадь для сорта 1: ")), int(input("Введите площадь для сорта 2: "))
year = 1
while (s1 / s2) > 0.1:
    s1 *= 2
    s2 *= 3
    year += 1
print(f"Через {year} лет площадь первых сортов будет составлять меньше 10% от площади вторых сортов")

# Задание 3

n2 = int(input("Введите число: "))
initial_number = n2
digits_counter = 0
digits_sum = 0
while n2 > 0:
    digits_sum += n2 % 10
    digits_counter += 1
    n2 = n2 // 10
print(f"В введенном числе {initial_number} количество цифр равно {digits_counter}",
      f"Сумма цифр равна {digits_sum}",
      sep="\n"
)

# Задание 4

grandson_age = int(input("Введите возраст внука: "))
grandfather_age = int(input("Введите возраст деда: "))
year = 1
while grandfather_age / grandson_age != 2:
    grandfather_age += 1
    grandson_age += 1
    year += 1
print(f"Дед станет вдвое старше внука через {year} лет",
      f"Возраст деда - {grandfather_age}",
      f"Возраст внука - {grandson_age}",
      sep="\n"
)

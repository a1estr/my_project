# Задание 1

num = int(input("Введите целое число: "))
if num > 0:
    num += 1
print(num)

# Задание 2

num1, num2, num3 = (int(input("Введите 1-ое число: ")),
                    int(input("Введите 2-ое число: ")),
                    int(input("Введите 3-е число: "))
                    )
counter_nums = 0
if num1 > 0:
    counter_nums += 1
    if num2 > 0:
        counter_nums += 1
        if num3 > 0:
            counter_nums += 1
    else:
        if num3 > 0:
            counter_nums += 1
else:
    if num2 > 0:
        counter_nums += 1
        if num3 > 0:
            counter_nums += 1
    else:
        if num3 > 0:
            counter_nums += 1
print(f"Количество положительных чисел = {counter_nums}")

# Задание 3

year = int(input("Введите интересующий вас год: "))
if year > 0:
    if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0):
        days = 366
    else:
        days = 365
    print(f"В этом году {days} дней")
else:
    print("Введен некорректный год")

# Задание 4

week = {1: "понедельник",
             2: "вторник",
             3: "среда",
             4: "четверг",
             5: "пятница",
             6: "суббота",
             7: "воскресенье"
        }

week_day = int(input("Введите номер дня недели: "))
if week_day in week.keys():
    current_day = week[week_day]
    print(f"Это {current_day}")
else:
    print("Введен некорректный номер дня недели")

# # Задание 5 (без условных операторов)

# num_of_unit = int(input("Введите номер единицы массы тела от 1 до 5: "))
#
# units_of_mass = {1: "килограмм",
#                  2: "миллиграмм",
#                  3: "грамм",
#                  4: "тонна",
#                  5: "центнер"
# }
# mass = float(input(f"Введите массу тела в {units_of_mass[num_of_unit]}ах(x): "))
# conversion_to_kg = {1: mass * 1,
#                     2: mass * 10 ** (-6),
#                     3: mass * 10 ** (-3),
#                     4: mass * 10 ** 3,
#                     5: mass * 10 ** 2
# }
# mass_in_kg = conversion_to_kg[num_of_unit]
# print(f"Масса тела = {mass_in_kg} кг")

# Задание 5 (с условными операторами)

num_of_unit = int(input("Введите номер единицы массы тела от 1 до 5: "))

units_of_mass = {1: "килограмм",
                 2: "миллиграмм",
                 3: "грамм",
                 4: "тонна",
                 5: "центнер"
                 }
mass_in_kg = 0
if num_of_unit in units_of_mass.keys():
    mass = float(input(f"Введите массу тела в {units_of_mass[num_of_unit]}ах(x): "))
    if num_of_unit == 1:
        mass_in_kg = mass
    elif num_of_unit == 2:
        mass_in_kg = mass * 10 ** (-6)
    elif num_of_unit == 3:
        mass_in_kg = mass * 10 ** (-3)
    elif num_of_unit == 4:
        mass_in_kg = mass * 10 ** 3
    elif num_of_unit == 5:
        mass_in_kg = mass * 10 ** 2
    print(f"Масса тела = {mass_in_kg} кг")
else:
    print("Введен некорректный номер единицы массы тела")




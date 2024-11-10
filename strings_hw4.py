# Задание 1

str_wth_8_char = "test1234"
print("Первый символ:", str_wth_8_char[0])
print("Последний символ:", str_wth_8_char[-1])
print("Третий с начала:", str_wth_8_char[2])
print("Третий с конца:", str_wth_8_char[-3])
print("Длина строки:", len(str_wth_8_char))

# Задание 2

str_with_10_15_char = "test1234test"
print("Первые 8 символов:", str_with_10_15_char[0:8])
print("4 символа из центра:",
      str_with_10_15_char[(len(str_with_10_15_char) // 2 - 2):(len(str_with_10_15_char) // 2 + 2)]
)
print("Символы с индексами кратными 3:", str_with_10_15_char[3::3])
print("Перевернутая строка:", str_with_10_15_char[::-1])

# Задание 3

my_name = "my name is name"
split_my_name = my_name.split(" ")
split_my_name[3] = "Alexey"
print(" ".join(split_my_name))

# Задание 4

test_string = "Hello world!"
print("Буква w находится на месте - ", test_string.find("w"))
print("Количество букв l =", test_string.count("l"))
print("Вернет True, так как строка начинается с 'Hello':", test_string.startswith("Hello"))
print("Вернет False, так как строка не заканчивается на 'qwe':", test_string.endswith("qwe"))
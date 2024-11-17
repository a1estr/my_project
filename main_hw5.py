import functions_from_hw4 as hw4

# Функция 1

result_variables = hw4.work_with_variables()
print(result_variables)

# Функция 2

result_chart_from_str = hw4.get_chars_from_str(input("Введите строку длиной не менее 8 символов:"))
print(result_chart_from_str)

# Функция 3

my_name = "my name is name"
print(hw4.replace_2nd_name(my_name))

# Функция 4

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print("Общий список:", hw4.lists_intersection(a, b))

# Функция 5

list_with_duplicates = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
print("Список без дубликатов:", hw4.unique_values_in_list(list_with_duplicates))

# Функция 6

school = {
    "1a": 22,
    "1b": 23,
    "2b": 36,
    "6a": 25,
    "7b": 21
}
result_student_in_class = hw4.student_number_in_class(school)
if type(result_student_in_class) == tuple:
    selected_class, students_in_class = result_student_in_class
    print(f"Количество учеников в классе {selected_class} - {students_in_class}")
else:
    print(result_student_in_class)

# Функция 7

text_for_count = input("Введите произвольный текст: ")
result_text_count = hw4.most_frequent_letter_in_text(text_for_count)
letters_exist = result_text_count[0]
if letters_exist:
    most_frequent_letter, most_frequent_value = result_text_count[1], result_text_count[2]
    print(f"Cамая частая буква в тексте: {most_frequent_letter}",
      f"Oна встречается в тексте {most_frequent_value} раз(а)", sep="\n"
      )
else:
    print("Введенный текст не содержит букв")

# Функция 8

year = int(input("Введите интересующий вас год: "))
year_result = hw4.days_in_year(year)
if year_result:
    print(f"В этом году {year_result} дней")

# Функция 9
swimmers_results = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17
}
print(hw4.best_from_swimmers(swimmers_results))

# Функция 10

number = int(input("Введите число: "))
digits_counter, digits_sum = hw4.count_digits(number)
print(f"В введенном числе {number} количество цифр равно {digits_counter}",
      f"Сумма цифр равна {digits_sum}",
      sep="\n"
      )
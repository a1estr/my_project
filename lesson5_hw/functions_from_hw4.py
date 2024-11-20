# Функции будут вызываться в main_hw5.py файле

# Функция 1

def work_with_variables():
    """
    1. Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No".
    2. Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза,
    результат свяжите с переменной big_int.
    3. Измените значение, хранимое в переменной var_float, уменьшив его на единицу,
    результат свяжите с той же переменной.
    4. Разделите var_int на var_float, а затем big_int на var_float.
    Результат данных выражений не привязывайте ни к каким переменным.
    5. Измените значение переменной var_str на "NoNoYesYesYes". При формировании
    нового значения используйте операции конкатенации (+) и повторения строки (*).
    6. Выведите значения всех переменных.
    """
    var_int = 10
    print(type(var_int))
    var_float = 8.4
    print(type(var_float))
    var_str = "No"
    big_int = 3.5 * var_int
    print(type(big_int))
    var_float -= 1
    var_str = var_str * 2 + "Yes" * 3
    print(type(var_str))
    return var_int, var_float, var_str, big_int, var_int / var_float, big_int / var_float

# Функция 2

def get_chars_from_str(str_wth_8_char):
    """
    1. Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
    Извлеките из строки первый символ, затем последний, третий с начала и третий с
    конца. Измерьте длину вашей строки.
    """
    first_char = str_wth_8_char[0]
    last_char = str_wth_8_char[-1]
    third_char = str_wth_8_char[2]
    third_from_end_char = str_wth_8_char[-3]
    str_length = len(str_wth_8_char)
    if str_length >= 8:
        return first_char, last_char, third_char, third_from_end_char, str_length
    else:
        return "Строка меньше 8 символов"

# Функция 3

def replace_2nd_name(name: str) -> str:
    """
    3. Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.
    """
    return "my name is {}".format(name)

# Функция 4

def lists_intersection(list1: list, list2: list) -> list:
    """
    Даны списки:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
    Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
    """
    return list(set(list1) & set(list2))

# Функция 5

def unique_values_in_list(list1: list) -> list:
    """
    8. Есть список: [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
    оставить в нем только уникальные значения. !не использовать циклы
    """
    return list(set(list1))

# Функция 6

def student_number_in_class(school: dict):
    """
    2. Узнайте сколько человек в каком-нибудь классе.
    """
    print("Список классов в школе -", list(school.keys()))
    required_class = input("Введите интересующий вас класс: ")
    return required_class, school.get(required_class, None)

# Функция 7

def most_frequent_letter_in_text(text):
    """
    2) Дан текст, который содержит различные английские буквы и знаки препинания.
    Вам необходимо найти самую частую букву в тексте.
    Результатом должна быть буква в нижнем регистре.
    При поиске самой частой буквы, регистр не имеет значения, так что при подсчете
    считайте, что "A" == "а". Убедитесь, что вы не считайте знаки препинания, цифры и
    пробелы, а только буквы. Если в тексте две и больше буквы с одинаковой частотой,
    тогда результатом будет буква, которая идет первой в алфавите.
    """
    characters = list(text.lower())
    most_frequent_letter = ""
    most_frequent_value = 0

    letters = []
    for char in characters:
        if char.isalpha():
            letters.append(char)

    if letters:
        letter_counts = {}
        for key in letters:
            letter_counts[key] = letters.count(key)
            most_frequent_value = max(letter_counts.values())

        most_frequent_letters_list = []
        for key in letter_counts:
            if letter_counts[key] == most_frequent_value:
                most_frequent_letters_list.append(key)

        most_frequent_letter = min(most_frequent_letters_list)

    return bool(letters), most_frequent_letter, most_frequent_value

# Функция 8

def days_in_year(year: int):
    """
    3. Дан номер года (положительное целое число). Определить количество дней в
    этом году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366 дней.
    Високосным считается год, делящийся на 4, за исключением тех годов, которые
    делятся на 100 и не делятся на 400
    (например, годы 300, 1300 и 1900 не являются високосными, а 1200 и 2000 являются).
    """
    if year > 0:
        if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0):
            return 366
        else:
            return 365
    else:
        print("Введен некорректный год")

# Функция 9

def best_from_swimmers(swimmers_results: dict):
    """
    Дан словарь пловцов с их результатами.
    Напечатать лучший результат заплыва среди 6 участников.
    """
    best_swimmer = 0
    for swimmer in swimmers_results.items():
        if swimmers_results[swimmer[0]] == min(swimmers_results.values()):
            best_swimmer = swimmer
            break
    return best_swimmer

# Функция 10

def count_digits(num: int):
    """
    Дано целое число N (>0). Используя операции деления нацело
    и взятия остатка от деления, найти количество и сумму его цифр.
    """
    digits_counter = 0
    digits_sum = 0
    while num > 0:
        digits_sum += num % 10
        digits_counter += 1
        num = num // 10
    return digits_counter, digits_sum

# Задание 1

str1 = "Robin Singh"
str2 = "I love arrays they are my favorite"
str1_to_list1 = str1.split(" ")
str2_to_list2 = str2.split(" ")
print(str1_to_list1)
print(str2_to_list2)

# Задание 2

list1 = ["Ivan", "Ivanou"]
capital = "Minsk"
country = "Belarus"
print(f"Привет, {list1[0]} {list1[1]}! Добро пожаловать в {capital} {country}")

# Задание 3

list2 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(" ".join(list2))

# Задание 4

list_with_10_elements = [1, 2, 3, 4, 5, 6, 7 ,8 , 9, 10]
list_with_10_elements[2] = "third"
list_with_10_elements.pop(6)
print(list_with_10_elements)

# Задание 5

a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4,'e': 5}

keys_from_a_b = set(a.keys() | b.keys())
ab = {}
for key in keys_from_a_b:
    ab[key] = [a.get(key, None), b.get(key, None)]
print(ab)

# Задание 1*

arr = [1, 5, 2, 9, 2, 9, 1]
unique_number = 0
for i in arr:
    if arr.count(i) == 1:
        unique_number = i
print("Уникальное число в массиве:", unique_number)

# Задание 2*

text = input("Введите произвольный текст:")
characters = list(text.lower())  # список всех символов в одном регистре

# Получаем список, состоящий только из букв

letters = []
for i in characters:
    if i.isalpha():
        letters.append(i)

if letters:

# Получаем словарь, в котором подсчитаны для всех букв их частота

    letter_counts = {}
    for i in letters:
        letter_counts[i] = letters.count(i)

    most_frequent_value = max(letter_counts.values())

# Получаем список, в котором будут все буквы с максимальной частотой

    most_frequent_letters_list = []
    for i in letter_counts.keys():
        if letter_counts[i] == most_frequent_value:
            most_frequent_letters_list.append(i)

# Находим букву, которая будет первой в алфавите

    most_frequent_letter = min(most_frequent_letters_list)
    print(f"Cамая частая буква в тексте: {most_frequent_letter}",
          f"Oна встречается в тексте {most_frequent_value} раз", sep="\n"
    )
else:
    print("Введенный текст не содержит букв")

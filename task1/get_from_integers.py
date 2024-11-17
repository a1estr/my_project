"""
В условии данной задачи ошибка должна выводиться, если чисел меньше 3.
При этом сам файл с числами по условию должен состоять из не менее чем 4 элементов.
Я поставил условие появления ошибки, когда в файле меньше 4 элементов (а не 3).
На мой взгляд так будет логичнее.
"""

from random import randint

FILENAME = "integers1.txt"

with open(FILENAME, "w") as file:
    last_number_for_range = randint(1, 8)
    for line in range(1, 3):
        for number in range(1, last_number_for_range + 1):
            file.write((str(randint(1, 100)) + " "))
        file.write("\n")

with open(FILENAME, "r") as file:
    list_of_numbers = []
    for line in file:
        line = line.strip()
        numbers_list_str = line.split(" ")
        numbers_list_int = list(map(int, numbers_list_str))
        list_of_numbers.extend(numbers_list_int)
    print(f"Элементы в файле: {list_of_numbers}")
    if len(list_of_numbers) >= 4:
        print(f"Первый элемент: {list_of_numbers[0]}",
              f"Второй элемент: {list_of_numbers[1]}",
              f"Предпоследний элемент: {list_of_numbers[-2]}",
              f"Последний элемент: {list_of_numbers[-1]}", sep="\n"
              )
    else:
        print("В файле меньше 4 элементов")
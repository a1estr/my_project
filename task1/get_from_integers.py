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
    numbers_list_int = []
    for line in file:
        line = line.strip()
        numbers_list_str = line.split(" ")
        numbers_list_int.extend(list(map(int, numbers_list_str)))
    print(f"Элементы в файле: {numbers_list_int}")
    if len(numbers_list_int) >= 4:
        print(f"Первый элемент: {numbers_list_int[0]}",
              f"Второй элемент: {numbers_list_int[1]}",
              f"Предпоследний элемент: {numbers_list_int[-2]}",
              f"Последний элемент: {numbers_list_int[-1]}", sep="\n"
              )
    else:
        print("В файле меньше 4 элементов")
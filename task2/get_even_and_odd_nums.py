from random import randint

FILENAME = "integers2.txt"

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
    even_numbers_list = []
    odd_numbers_list = []
    for number in list_of_numbers:
        if number % 2 == 0:
            even_numbers_list.append(number)
        else:
            odd_numbers_list.append(number)

with open("even_numbers.txt", "w") as file:
    if even_numbers_list:
        for number in even_numbers_list:
            file.write(str(number) + " ")

with open("odd_numbers.txt", "w") as file:
    if odd_numbers_list:
        for number in odd_numbers_list:
            file.write(str(number) + " ")



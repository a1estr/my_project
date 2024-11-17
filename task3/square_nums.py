from random import randint, uniform

FILENAME = "floats.txt"

with open(FILENAME, "w") as file:
    last_number_for_range = randint(10, 20)
    for number in range(1, last_number_for_range + 1):
        random_number = round(uniform(1, 100), randint(1, 3))
        file.write(str(random_number) + " ")

with open(FILENAME, "r") as file:
     for line in file:
         numbers_list_str = (line.strip()).split(" ")
         numbers_list_float = list(map(float, numbers_list_str))
         print("Вещественные числа в исходном файле:", numbers_list_float)
         def num_square_in_list(nums_list:list) -> list:
             end = len(nums_list)
             for i in range(0, end):
                 nums_list[i] = nums_list[i] ** 2
             return nums_list
         num_square_in_list(numbers_list_float)

print("Вещественные числа в квадрате:", numbers_list_float)

with open(FILENAME, "w") as file:
     for number in numbers_list_float:
         file.write(str(number) + " ")



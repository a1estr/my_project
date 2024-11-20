# не придумал как решить это задание без использования цикла

numbers = [1, 5, 2, 9, 2, 9, 1]
for i in numbers:
    if numbers.count(i) == 1:
        unique_number = i
print(f"Уникальное число в массиве {unique_number}")

# нужно учитывать, сколько раз будет считаться цикл
# (система может быть перегружена, если много раз повторяется -> оптимизируем)

arr_2 = [1, 5, 2, 9, 2, 9, 1]
unique_number_2 = 0
for i in arr_2:
    unique_number_2 ^= i
print(unique_number_2)
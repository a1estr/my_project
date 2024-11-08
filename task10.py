# не придумал как решить это задание без использования цикла

numbers = [1, 5, 2, 9, 2, 9, 1]
for i in numbers:
    if numbers.count(i) == 1:
        unique_number = i
print(f"Уникальное число в массиве {unique_number}")

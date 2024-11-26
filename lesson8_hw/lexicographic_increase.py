from random import randint


def generate_numbers():
    numbers_list = []
    last_number_for_range = randint(1, 100)
    for i in range(1, last_number_for_range):
        number = randint(0, 19)
        numbers_list.append(str(number))
    return " ".join(numbers_list)


numbers_str = generate_numbers()
print("Исходная последовательность чисел:",
      numbers_str,
      sep="\n"
      )

NUMBER_NAMES = {0: 'zero',
                1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine',
                10: 'ten',
                11: 'eleven',
                12: 'twelve',
                13: 'thirteen',
                14: 'fourteen',
                15: 'fifteen',
                16: 'sixteen',
                17: 'seventeen',
                18: 'eighteen',
                19: 'nineteen'
                }

numbers_list = numbers_str.split(" ")
numbers_list = list(map(int, numbers_list))
numbers_dict = {}
for number in numbers_list:
    numbers_dict.setdefault(NUMBER_NAMES[number], []).append(number)

sorted_numbers_dict = dict(sorted(numbers_dict.items(),
                                  key=lambda item: item[0]
                                  )
                           )

sorted_numbers_list_with_lists = list(sorted_numbers_dict.values())
sorted_numbers_list = []
for list_i in sorted_numbers_list_with_lists:
    sorted_numbers_list.extend(list_i)

sorted_numbers_list = list(map(str, sorted_numbers_list))
sorted_numbers_str = " ".join(sorted_numbers_list)
print("Отсортированная последовательность чисел:",
      sorted_numbers_str,
      sep="\n"
      )

# Задание 1

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]


def create_gen_with_positive_nums(numbers_list):
    for num in numbers_list:
        if num > 0:
            yield num


generator_of_positive_nums = create_gen_with_positive_nums(numbers)
print(type(generator_of_positive_nums), generator_of_positive_nums)
for num in generator_of_positive_nums:
    print(num)

# Задание 2

sentence = "thequick brown fox jumps over the lazy dog"
words_in_sentence = sentence.split(" ")
words_len_in_sentence = []

for word in words_in_sentence:
    try:
        if word == "the":
            raise Exception
        words_len_in_sentence.append(len(word))

    except:
        print('Найдено слово "the"')
print(words_len_in_sentence)

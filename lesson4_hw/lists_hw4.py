# Задание 1

list1 = [1, 2, 3, 4, 5]
list2 = ["test1", "test2", "test3", "test4"]

# Задание 2

second_from_list1 = list1[1]

# Задание 3

list2[3] = "edited_test4"
print(list2)

# Задание 4

merged_list = list1 + list2
print(merged_list)

# Задание 5

from_merged_list = merged_list[3:7]
print(from_merged_list)

# Задание 6

with_added_elements = from_merged_list.extend(["new element", 17])
print(from_merged_list)

# Задание 7

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

intersection_list =list(set(a) & set(b))
print(intersection_list)

# Задание 8

list_with_duplicates = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
list_without_duplicates = list(set(list_with_duplicates))
print(list_without_duplicates)
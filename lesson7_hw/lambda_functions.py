# Задание 1

lambda_hello = lambda name: f"Hello, {name}"
entered_name = input("Enter your name: ")
print(lambda_hello(entered_name))

# Задание 2

lambda_hello_list = lambda names: list(map(lambda_hello, names))

names_list = [input("Enter the name: ") for name in range(4)]
list_with_hello_names = lambda_hello_list(names_list)
print(list_with_hello_names)

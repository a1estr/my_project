def typed(defined_type):
    def decorator(func):
        def wrapper(*args):
            list_args = list(args)
            if defined_type == "str":
                for i in range(len(list_args)):
                    if not isinstance(list_args[i], str):
                        list_args[i] = str(list_args[i])
            elif defined_type == "int":
                for i in range(len(list_args)):
                    if isinstance(list_args[i], str):
                        list_args[i] = int(list_args[i])
            return func(*list_args)

        return wrapper

    return decorator


@typed(defined_type="str")
def add_two_symbols(a, b):
    return a + b


print("Декоратор с типом 'str':")
print(add_two_symbols("3", 5.1))
print(add_two_symbols(5, 5))
print(add_two_symbols("a", "b"))


@typed(defined_type="int")
def add_three_symbols(a, b, c):
    return a + b + c


print("Декоратор с типом 'int':")
print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))

string = input("Введите строку:")
print("Строка с пробелом в начале и конце:", '"' + string + '"')
print("Строка без пробела в начале и в конце:", '"' + string[1:-1] + '"')
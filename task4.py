full_name = "Ivanou Ivan"

# разделили введенную строку отдельно на имя и фамилию => получили список

split_full_name = full_name.split(" ")

# выведем теперь сначала имя, а затем фамилию

print(split_full_name[1] + " " + split_full_name[0])
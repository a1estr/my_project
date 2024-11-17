with open("file1.txt", "w") as file:
    file.writelines(["Content of the FIRST file:\n", "FILE 1 - test\n", "End of the FIRST file.\n"])

with open("file2.txt", "w") as file:
    file.writelines(["Content of the SECOND file:\n", "FILE 2 - test\n", "End of the SECOND file.\n"])


with open("file1.txt", "r") as file:
    file1_content = file.readlines()
print(file1_content)

with open("file2.txt", "r") as file:
    file2_content = file.readlines()
print(file2_content)

with open("file1.bin", "wb") as file:
    for line in file2_content:
        file.write(line.encode())

with open("file2.bin", "wb") as file:
    for line in file1_content:
        file.write(line.encode())



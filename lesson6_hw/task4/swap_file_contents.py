with open("file1.bin", "wb") as file:
    file.writelines(["Content of the FIRST file:\n".encode(),
                     "FILE 1 - test\n".encode(),
                     "End of the FIRST file.\n".encode()
                     ])

with open("file2.bin", "wb") as file:
    file.writelines(["Content of the SECOND file:\n".encode(),
                     "FILE 2 - test\n".encode(),
                     "End of the SECOND file.\n".encode()
                     ])

with open("file1.bin", "rb") as file:
    file1_content = []
    for line in file:
        line = line.decode()
        file1_content.append(line)
print("Содержимое первого файла:", file1_content)

with open("file2.bin", "rb") as file:
    file2_content = []
    for line in file:
        line = line.decode()
        file2_content.append(line)
print("Содержимое второго файла:", file2_content)

with open("file1.bin", "wb") as file:
    for line in file2_content:
        file.write(line.encode())

with open("file2.bin", "wb") as file:
    for line in file1_content:
        file.write(line.encode())



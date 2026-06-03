import os

file_path = "./lab8.txt"

if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        file.write("New file created. \n")
        print("File created. ")

with open(file_path, "a") as file:
    file.write("Appending new line. \n")
    print("File appended. ")

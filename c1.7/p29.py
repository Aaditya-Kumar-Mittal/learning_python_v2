with open("sample.txt", "a") as file:
    file.write("This is a new line added to the file.\n")
    file.write("Appending another line to the file.\n")

with open("sample.txt", "r") as file:
    data = file.read()
    print(data)
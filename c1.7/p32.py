with open("demo.txt", "r") as f:
    data = f.read()
    findPython = data.find("Python")
    if findPython != -1:
        print("Python is present in the file.")
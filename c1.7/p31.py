with open("demo.txt", "r") as f:
    data = f.read()
    
new_data =data.replace("Java", "Python")

with open("demo.txt", "w") as f:
    f.write(new_data)
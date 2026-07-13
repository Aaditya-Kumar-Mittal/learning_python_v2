with open("demo.txt", "a") as f:
    f.write("Hi everyone\n")
    f.write("learning Java I/O\n")
    f.write("using Java.\n")
    f.write("I like Java Programming.\n")

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
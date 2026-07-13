# Opening a file in read mode
# f = open('file_name', 'mode')
# default mode is 'r' which is read mode
file = open('sample.txt', 'r')

data = file.read()
print(data)
print(type(data))  # Printing the type of data read from the file

file.close()  # Closing the file after reading
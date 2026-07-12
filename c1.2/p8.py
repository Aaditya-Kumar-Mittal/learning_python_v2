firstName = input("Enter your first name: ")
print(f"First name is {firstName}")
print(f"Length of First Name is {len(firstName)}")

sampleStr = "#########%%%%%%%%%######33$$$$$$$$$$$4##########33$$$$$$$$$$"
findChar  = input("Enter a character to find in the string: ")

if findChar in sampleStr:
    print(f"Character '{findChar}' is present in the string.")
    print(f"Count of '{findChar}' in the sample string is: {sampleStr.count(findChar)}")
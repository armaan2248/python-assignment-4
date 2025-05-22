try:
    file = open("sample.txt", "r")
    reading_file = file.read()
    print("Read file contents: ")
    print(reading_file)
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

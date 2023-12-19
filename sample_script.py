#import os

def write_file():
    # Create a new file and write some text to it
    with open('languages.txt', 'w') as file_handler:
        file_handler.write("Bash\\n")
        file_handler.write("Python\\n")
        file_handler.write("PHP\n")

def read_file():
    # Open the file and read its contents
    with open('languages.txt', 'r') as file_handler:
        for line in file_handler:
            print(line)

# Write to and read from the file
_write_file()
read_file()
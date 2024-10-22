# file_handling_assignment.py

# File Creation and Writing
try:
    # Creating a new file and opening it in write mode
    file = open("my_file.txt", "w")
    
    # Writing three lines of text with a mix of strings and numbers
    file.write("Line 1: Hello, World!\n")
    file.write("Line 2: The year is 2024.\n")
    file.write("Line 3: Python is amazing with PLP!\n")
    print("File created and initial content written successfully.")
    
except PermissionError:
    print("Permission denied: Unable to write to the file.")
finally:
    # Ensure the file is closed
    file.close()

# File Reading and Displaying Contents
try:
    # Opening the file in read mode to display its contents
    file = open("my_file.txt", "r")
    
    # Reading and displaying the contents
    print("\nContents of 'my_file.txt':")
    print(file.read())
    
except FileNotFoundError:
    print("File not found: Unable to read the file.")
finally:
    # Ensure the file is closed
    file.close()

# File Appending
try:
    # Opening the file in append mode to add more lines
    file = open("my_file.txt", "a")
    
    # Appending three additional lines of text
    file.write("Line 4: Appending new content.\n")
    file.write("Line 5: Coding is fun and amazing!\n")
    file.write("Line 6: Let's keep learning and explole the World.\n")
    print("\nAdditional content appended successfully.")
    
except PermissionError:
    print("Permission denied: Unable to append to the file.")
finally:
    # Ensure the file is closed
    file.close()

# Reading the file again to show the final content
try:
    # Opening the file in read mode to display its updated contents
    file = open("my_file.txt", "r")
    
    # Reading and displaying the updated contents
    print("\nFinal contents of 'my_file.txt':")
    print(file.read())
    
except FileNotFoundError:
    print("File not found: Unable to read the file.")
finally:
    # Ensure the file is closed
    file.close()

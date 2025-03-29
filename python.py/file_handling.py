#File handling in Python allows you to work with files for reading, writing, and updating data.Python provides built-in functions to open, manipulate, and close files in an efficient and easy manner.


#Basic File Operations:
#The most common operations you can perform on files are:

#Opening a file: To open a file, you need to specify the file path and mode.
#Reading from a file: Read the contents of a file.
#Writing to a file: Write new data into a file.
#Closing a file: Always close a file after completing operations to free up system resources.

#File Handling Modes:
#Mode	Description
#"r"	Read mode. Opens the file for reading.
#"w"	Write mode. Opens the file for writing (overwrites the file).
#"a"	Append mode. Opens the file for appending (adds new data at the end).
#"x"	Create mode. Creates a new file (raises an error if the file already exists).
#"b"	Binary mode. Opens the file in binary mode (for files like images, etc.).
#"t"	Text mode. Opens the file in text mode (default mode for text files).

#Syntax:
#file_object = open(file_name, mode)

#Write the new file
f = open('my_file.txt', 'w')

f.write('This is suri\nFrom Vijayawada\nSoftware Engineer')
f.close()
print('file created successfully')

#Read the file
f = open('my_file.txt', 'r')
content = f.read()
print(content)

#Append the file
f = open('my_file.txt', 'a')
f.write('\nIntrest to learn new things\ndedicated to Automation testing')
f.close()
print('Updated')


#After Updated again i am reading the file
#Read the file
f = open('my_file.txt', 'r')
content = f.read()
print(content)



#using with
with open('my_file.txt', 'r') as file:
    content = file.read()
    print('USING WITH')
print(content)




#Creating a csv file:
import csv
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    print(writer)

    #Header
    writer.writerow(['Name','Age','Place','Job'])

    #Fields
    writer.writerow(['Suri',24,'Chennai','Software'])
    writer.writerow(['Harika',23,'Banglore','HR Operations'])
    writer.writerow(['Pandu',21,'Vijayawada','Student'])


import csv
with open('data.csv', 'r') as file:
    ss = csv.reader(file)

    for row in ss:
        print(row)

import csv
with open('data.csv', mode='a', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['babu',25,'Hyderabad','Doctor'])
print('yes')

import csv
with open('data.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)



#Creating text file
# Write to a text file
with open('file.txt', mode='w') as file:
    # Write header (if needed)
    file.write("Name,Age,Marital_status,Gender\n")
    
    # Write rows of data
    file.write("Suri,25,Nope,Male\n")
    file.write("Pandu,23,Nope,Female\n")
    file.write("Babu,27,Nope,Male\n")
    file.write("Harika,24,Nope,Female\n")

# Read from the text file
with open('file.txt', mode='r') as file:
    # Print the content of the file
    print("Reading file content:")
    for line in file:
        print(line.strip())  # Remove newline characters for cleaner output

# Append new data to the text file
with open('file.txt', mode='a') as file:
    # Append new rows
    file.write("Amma,37,Married,Female\n")

# Read again to verify the appended content
with open('file.txt', mode='r') as file:
    print("\nAfter appending:")
    for line in file:
        print(line.strip())

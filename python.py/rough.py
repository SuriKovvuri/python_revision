file = open('rough.txt', 'w')
file.write('Hello This is suri\nFrom Vijayawda\nSoftware engineer\nIn Chennai')
file.close()
print('New Text File Created!')

#Read the creted file:
file = open('rough.txt', 'r')
read_file = file.read()
print('Read the new file : ')
print(read_file)

#Updating the file:
file = open('rough.txt', 'a')
file.write('\nThank you')
file.close()
print('Updated the text file')

#Read the updated file:
file = open('rough.txt', 'r')
updated_file = file.read()
print('Display the Updated code :')
print(updated_file)

#with
with open('rough.txt', 'r') as file:
    content = file.read()
    print('Open with : ')
print(content)

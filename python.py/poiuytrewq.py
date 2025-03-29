# import csv
# with open("poiuytrewq.csv",mode='w', newline='') as file:
#     writer = csv.writer(file)
#     print(writer)
    
#     writer.writerow(['Name','age','city'])
    
#     writer.writerow(['ss',25,'Chennai'])
    
    
# with open('poiuytrewq.csv', mode='r')as file:
#     read = csv.reader(file)
#     for row in read:
#         print(row)
    


# # Step 1: Append a new row to the CSV file
# with open("poiuytrewq.csv", mode='a', newline='') as file:
#     writer = csv.writer(file)
    
#     # Adding a new row with just "a"
#     writer.writerow(['a',2,'kkk'])

# print("Row added to CSV file.\n")


    
with open('poiuytrewq.txt', 'w') as file:
    file.write("Hi This is Suri\nFrom Vijayawada\nThank you")

with open('poiuytrewq.txt', 'r') as file:
    content = file.read()
    print(content)
    
with open('poiuytrewq.txt', 'a') as file:
    file.write("\nHehe")

with open('poiuytrewq.txt', 'r') as file:
    content = file.read()
    print(content)
    
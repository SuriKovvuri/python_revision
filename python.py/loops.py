#for Loop:for loop in Python is used to iterate over sequences such as lists, tuples, strings, or even ranges.
#syntax:
#for variable in sequence:
    # code block to execute
# Iterating over a List
fruits = ["apple", "banana", "orange", "mango"]
for list in fruits:
    print(list)

# Iterating over a String
for letters in "python":
    print(letters)

# Using range()
for i in range(5):
    print(i)

#using break
for i in range(10):
    if i == 5:
        break
    print(i)

#continue
for i in range(5):
    if i == 3:
        continue
    print(i)

#summing numbers in List
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num  # Adds each number to total

print("Sum:", total)




#Real time example:
shopping_cart = [
        {'item':'laptop','price':1000},
        {'item':'shirt','price':500},
        {'item':'pant','price':2000}
        ]
print(shopping_cart)
total_sum = 0
for shopping in shopping_cart:
    total_sum += shopping["price"]
    print(total_sum)
print(f"Total money spent for shopping: ${total_sum}")












#While Loop:while loop repeats the block of code as long as a condition remains true. If the condition becomes False, the loop ends.
#syntax:
#while condition:
    # code block to execute

i = 1;
while i <= 5:
    print(i)
    i += 1



#Infinite while Loop
i = 1
while True:
    print(i)
    i += 1
    if i >= 5:
        break





















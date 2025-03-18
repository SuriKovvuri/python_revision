'''
Armstrong or not
'''
def is_armstrong(num):
    # Get the digits of the number
    digits = str(num)
    power = len(digits)
    print(f"Number: {num}, Digits: {digits}, Power: {power}")
    
    # Calculate the sum of each digit raised to the power of the number of digits
    total = 0
    for d in digits:
        digit_power = int(d) ** power
        total += digit_power
        print(f"Digit: {d}, {d}^{power} = {digit_power}, Running Total: {total}")
    
    # Final comparison
    print(f"Final Sum: {total}")
    if total == num:
        print(f"{num} is an Armstrong number.\n")
        return True
    else:
        print(f"{num} is NOT an Armstrong number.\n")
        return False

# Test cases
is_armstrong(153)
is_armstrong(9474)
is_armstrong(123)



'''
Reverse a String
'''

#reverse a string
def reverse_string(s):
    return s[::-1]
# Example
print(reverse_string("hello"))  # Output: "olleh"


def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
        print(reversed_str)
    return reversed_str
# Example
print(reverse_string("hello"))  # Output: "olleh"


def reverse_string(s):
    return "".join(reversed(s))
# Example
print(reverse_string("hello"))  # Output: "olleh"





#plaindrome
def is_palindrome_number(num):
    s = str(num)
    return s == s[::-1]
# Test cases
print(is_palindrome_number(121))  # True
print(is_palindrome_number(123))  # False


def is_palindrome(s):
    return s == s[::-1]
# Test cases
print(is_palindrome("radar"))   # True
print(is_palindrome("python"))  # False


'''
Palindrome or not
'''
def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case insensitivity
    length = len(s)
    
    for i in range(length // 2):
        print(f"Comparing {s[i]} with {s[length - i - 1]}")  # Print each comparison
        if s[i] != s[length - i - 1]:
            print("Not a palindrome ❌")
            return False
    print("It's a palindrome ✅")
    return True

def is_palindrome_number(n):
    s = str(n)  # Convert number to string
    length = len(s)
    
    for i in range(length // 2):
        print(f"Comparing {s[i]} with {s[length - i - 1]}")  # Print each comparison
        if s[i] != s[length - i - 1]:
            print("Not a palindrome ❌")
            return False
    print("It's a palindrome ✅")
    return True

# Example usage:
num = 12321
is_palindrome_number(num)

# Example usage
text = input("Enter a string: ")
is_palindrome(text)



'''
#Factorial of a Number
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1) #recursive

# Step-by-Step Execution for factorial(5)
# factorial(5) → 5 * factorial(4)
# factorial(4) → 4 * factorial(3)
# factorial(3) → 3 * factorial(2)
# factorial(2) → 2 * factorial(1)
# factorial(1) → 1 (Base Case Reached!)
# Now, returning values back up:
# factorial(2) = 2 * 1 = 2
# factorial(3) = 3 * 2 = 6
# factorial(4) = 4 * 6 = 24
# factorial(5) = 5 * 24 = 120

# Test cases
print(factorial(5))  # 120
print(factorial(0))  # 1



'''
#Prime number or not
'''
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
# Test cases
print(is_prime(7))  # True
print(is_prime(10)) # False



# Find the Largest Element in a Lists
def find_largest(arr):
    return max(arr) #for min min(arr)
# Test cases
print(find_largest([1, 5, 3, 9, 2])) # 9
print(find_largest([-1, -5, -3, -9])) # -1


'''
#Find First largest and First smallest
'''
# Find the Largest Element in a Lists
n = [2,3,1,7,99,2,4,79]
max = n[0]
for num in n:
    # print(num)
    if max < num:
        max = num
print(max)


# Find the smallest Element in a Lists
n = [2,3,1,7,99,2,4,79]
max = n[0]
for num in n:
    # print(num)
    if max > num:
        max = num
print(max)

'''
#Find second largest and second smallest
'''
# List of numbers
n = [2, 3, 1, 7, 99, 2, 4, 79]

sort_data = sorted(set(n))
print(sort_data)

print(sort_data[1])
print(sort_data[-2])




# Find Duplicates in an Array
def find_duplicates(arr):
    duplicates = []
    seen = set()
    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

# fibonacci with recursive
'''
 where a function calls itself in order to solve a smaller instance of the same problem. A function that uses recursion is called a recursive function.
In a recursive function, two main things are required:
Base case: A condition that stops the recursion to prevent infinite calls.
Recursive case: The function calls itself with a smaller input to work toward the base case
'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))


a, b = 0, 1  # Starting values for Fibonacci sequence
for i in range(10):
    print(a)
    a, b = b, a + b  # Update a and b in a single line


def fibonacci(n):
    a, b = 0, 1
    sequence = []  # To store the Fibonacci sequence
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence  # Return the full sequence

print(fibonacci(10))
#Logic
# Step 1: a = 0, b = 1
# Step 2: a = 1, b = 1
# Step 3: a = 1, b = 2
# Step 4: a = 2, b = 3
# Step 5: a = 3, b = 5
# Step 6: a = 5, b = 8
# Step 7: a = 8, b = 13
# Step 8: a = 13, b = 21
# Step 9: a = 21, b = 34
# Step 10: a = 34, b = 55
# Final Fibonacci Series: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


#Remove duplicates
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)  # Order is not guaranteed



my_list = [1, 2, 2, 3, 4, 4, 5]
seen = set()  # Create an empty set to track seen items
unique_list = []  # Create an empty list to store unique items
# Loop through each element in the original list
for x in my_list:
    print(x)
    if x not in seen:  # If the element has not been seen before
        unique_list.append(x)  # Add it to the unique list
        seen.add(x)  # Mark it as seen by adding it to the set

print(unique_list)  # Output: [1, 2, 3, 4, 5]


# count the characters in a string
text = "Hello, world!"
count = len(text)
print(count)  # Output: 13



'''
Remove spaces using replace
'''
data = "This is Suri From"
replace = data.replace(" ", "")
print(replace)

#Count with-out spaces
text = "Hi this is so and so"
count = len(text.replace(" ", ""))  # Remove spaces before counting
print(count)



'''
Find Common elemnts in two arrays
'''
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
common_elements = [x for x in a if x in b]  # Check each element of 'a' in 'b'
print(common_elements)  # Output: [2, 3, 4]




#sum of numbers in a list
my_list = [1, 2, 3, 4, 5]
total = sum(my_list)
print(total)  # Output: 15

#2nd model
my_list = [1, 2, 3, 4, 5]
total = 0
for num in my_list:
    total += num  # Add each number to total
print(total)  # Output: 15



#sum of numbers in a list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = [a + b for a, b in zip(list1, list2)]
print(result)  # Output: [5, 7, 9]




#add two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]


#number of vowels in a string
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
s = "Thi is a suri"
vowel_count = sum(1 for char in s if char in vowels)
consonant_count = sum(1 for char in s if char in consonants)
print(vowel_count)
print(consonant_count)


'''
Count the digits and alphabets
'''
data = "1g2hv3h4h4g3vh5gv3hhg2v4v5mb7mnb7v"

digit_count = sum(1 for char in data if char.isdigit())  # Count digits
alphabet_count = sum(1 for char in data if char.isalpha())  # Count alphabets

print(f"Number of digits: {digit_count}")
print(f"Number of alphabets: {alphabet_count}")



#swap numbers with temp
a = 5
b = 10
#using temp values
temp = a
a = b
b = temp
#printing
print(a)
print(b)


#without temp values
a = 5
b = 20
a,b = b,a
print(a)
print(b)

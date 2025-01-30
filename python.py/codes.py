# armstrong
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


#Factorial of a Number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Test cases
print(factorial(5))  # 120
print(factorial(0))  # 1


#Prime number or not
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


def fibonacci_iterative(n):
    a, b = 0, 1
    series = []
    for i in range(n):
        print(f"Step {i+1}: a = {a}, b = {b}")  # Log the values of a and b
        series.append(a)
        a, b = b, a + b  # Update values
    return series

# Generate the first 10 Fibonacci numbers
result = fibonacci_iterative(10)
print(f"Final Fibonacci Series: {result}")
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
    if x not in seen:  # If the element has not been seen before
        unique_list.append(x)  # Add it to the unique list
        seen.add(x)  # Mark it as seen by adding it to the set

print(unique_list)  # Output: [1, 2, 3, 4, 5]

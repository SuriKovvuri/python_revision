#Decision making statements:
# if
#syntax:
#if condition: -->if condion is True, Then excutes the inside if block of code.

a = 25
b = 100
if b > a:
    print('b greaterthan a')
    print('condition pass')
    pass

#if-else : 
#syntax:
#    if condition:
#    # Code block if condition is True
#else:
#    # Code block if condition is False
    
if a > b:
    print('a is greaterthan b condition failed')
else:
    print('b is greaterthan a condition pass')


#if-elif-else Statement
#The elif (short for "else if") clause allows you to check multiple conditions. If the first condition is false, the program checks the next condition, and so on. The else block is executed only if none of the conditions are true.
#syntax:
#if condition1:
    # Code block if condition1 is True
#elif condition2:
    # Code block if condition2 is True
#else:
    # Code block if none of the conditions are True

x = 15
if x > 20:
    print('15 is greater than 20')
elif x < 20:
    print('15 is lessthan 20, so condition passed')
else:
    print('nothing true')


#Nested-if
# Input : input: Given a person age & gender if a person gender is male & age is below 30 then print '30 blow male'
#age = int(input("Enter your age: "))
#gender = input("Enter your gender (male/female): ").lower()
age = 28;
gender = 'male'
# Nested if structure
if gender == "male":  # Outer if: check if gender is male
    if age < 30:  # Inner if: check if age is below 30
        print("30 below male")
    else:  # Age is 30 or above
        print("30 or above male")
else:  # Gender is not male (assumed to be female)
    print("Person is female")


#Short-Hand if Statement
#syntax
#if condition: action
x = 10
if x > 5: print('10 is greaterthan 5')

#Short-Hand if-else
#syntax:
#action_if_true if condition else action_if_false
y = 20
print("20 is lessthan 30") if y < 30 else print("20 is greaterthan 30")





#pass statement
x = 10
if x > 5:
    pass  # This means "do nothing" for now
else:
    print("x is less than or equal to 5")



#Comparison Operators for Conditions:
#In Python, conditions are formed using comparison operators:

#== : Equals
#!= : Not Equals
#> : Greater Than
#< : Less Than
#>= : Greater Than or Equal To
#<= : Less Than or Equal To

x = 10
if x == 10:
    print("x is 10")
if x != 5:
    print("x is not 5")


#Logical Operators:
#You can combine conditions using logical operators:

#and: Both conditions must be true.
#or: At least one condition must be true.
#not: Negates the condition.
x = 10
y = 5

if x > 5 and y < 10:
    print("Both conditions are true")
if x > 5 or y > 10:
    print("At least one condition is true")
if not(x < 5):
    print("x is not less than 5")





age = int(input("Enter your age: "))
gender = input("Enter your gender (male/female): ").lower()

if age > 18:
    print("Eligible to vote")

    if gender == "male":
        print("This male has the right to vote.")
    else:
        print("This female has the right to vote.")  # Corrected message here
else:
    print("Not eligible to vote")


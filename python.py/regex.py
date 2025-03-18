#regex is a powreful tool which is used to  matching pattern and text processing
#import re
#matching, searching and replacing 
import re 

#Matches any whitespace character (space, tab, newline, etc.).
#Inside the negated set, it means "any character that is not a whitespace."
 
# Extract Words From a Sentence
pattern = '[^\d\s]+'
data = "The quick brown fox jumps over 13 lazy dogs."
res = re.findall(pattern, data)
print(res)


# Find Digits in a String
pattern = '\d+'
data = "My number is 12345, and my friend's number is 67890."
resp = re.findall(pattern,data)
print(resp)


# Match Email Addresses
# pattern = 'support@example.com'
pattern = '\S+@\S+'
data = "Contact us at support@example.com, sales@shop.com, or info@company.org."

respp= re.findall(pattern,data)
print(respp)
# Use a raw string to correctly interpret \b as a word boundary


# Find Words Starting With a Specific Letter
pattern =  r'\b[aA]\w*'

data = "Apple, banana, apricot, cherry, avocado."

resppp = re.findall(pattern, data)
print(resppp)




# match the pattern
import re
email = "test@example.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if re.match(pattern, email):
    print("Valid email!")
else:
    print("Invalid email!")

# search = re.match(pattern, email)
# print(search)


# Extract Numbers
import re
text = "The price is 100 dollars 200 and 300."
numbers = re.findall(r"\d+", text)
print(numbers)  # Output: ['100']

import re
text = "Python 123 is 456 great 789!"
result = re.sub(r"\d+", "", text)
print(result)

#Replace spaces
import re
text = "Hello World!"
result = re.sub(r"\s+", "-", text)
print(result)  # Output: "Hello-World!"

# remove spaces
text = "Hello World!"
result = re.sub(r"\s+", "", text)
print(result)  # Output: "Hello-World!"


#searching
import re
text = "Python is great!"
result = re.search(r"is", text)
if result:
    print(f"Found '{result.group()}' at index {result.start()}.")
else:
    print("Pattern not found.")


#matching
import re
text = "Python is great!"
result = re.match(r"Python", text)
if result:
    print(f"Matched '{result.group()}' at the beginning of the string.")
else:
    print("Pattern not matched at the start.")

'''
Key Difference from re.search:

re.match only checks the start of the string.
re.search looks for the pattern anywhere in the string.
'''

'''
Function	Purpose	Return Value
re.search	Finds the first occurrence of a pattern anywhere in the string.	Match object or None
re.match	Checks if the pattern matches at the beginning of the string.	Match object or None
re.sub	Replaces all occurrences of a pattern with a replacement string.	Modified string
re.findall	Finds all non-overlapping occurrences of a pattern.	List of matches

'''
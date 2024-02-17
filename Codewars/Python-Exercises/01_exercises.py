"""
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.
"""

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    
print(basic_op("+", 4, 7))

"""Write a function that removes the spaces from the string, then return the resultant string."""
def no_space(x):
    return x.replace(" ", "")


x = "8 j 8   mBliB8g  imjB8B8  jl  B"
print(no_space(x))

"""Complete the method that takes a boolean value and 
return a "Yes" string for true, or a "No" string for false."""

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
    
print(bool_to_word(True))

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

print(bool_to_word(False))

"""
Write a function that takes an array of numbers and returns 
the sum of the numbers. The numbers can be negative or non-integer. 
If the array does not contain any numbers then you should return 0.
"""

def sum_array(a):
    if len(a) == 0:
        return 0
    total = 0
    for i in a:
        total += i
    return total

lst = [1, 5.2, 4, 0, -1]   
print(sum_array(lst))

def sum_array(a):
  return sum(a)

lst = [1, 5.2, 4, 0, -1]   
print(sum_array(lst))

def get_grade(s1, s2, s3):
    score = abs(sum([s1, s2, s3]) / 3)
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    elif score < 60:
        return "F"
    

print(get_grade(90,95,93))

def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3.0
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    return "F"

print(get_grade(44, 100, 100))
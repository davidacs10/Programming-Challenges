"""Given a non-empty array of integers, return the result 
of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24"""

def grow(arr):
    total = 1
    for num in arr:
        total *= num
    return total


nums = [1, 2, 3, 4]
print(grow(nums))

"""
Given a set of numbers, return the additive inverse of each. 
Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []

You can assume that all values are integers. 
Do not mutate the input array/list."""

def invert(lst):
    num_list = []
    for num in lst:
        num = -num
        num_list.append(num)
    return num_list
        
print(invert([1,2,3,4,5]))

def invert(lst):
    return [-x for x in lst]

print(invert([1,2,3,4,5]))

"""Consider an array/list of sheep where some sheep may be 
missing from their place. We need a function that counts the 
number of sheep present in the array (true means present).

For example,
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]"""

def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i is True:
            count += 1
    return count

sheeps = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

print(count_sheeps(sheeps))

"""This function should test if the factor is a factor of base.
Return true if it is a factor or false if it is not.

About factors
Factors are numbers you can multiply together to get another number.
2 and 3 are factors of 6 because: 2 * 3 = 6
You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
You can use the mod operator (%) in most languages to check for a remainder
For example 2 is not a factor of 7 because: 7 % 2 = 1

Note: base is a non-negative number, factor is a positive number."""

def check_for_factor(base, factor):
    if base % factor == 0:
        return True
    if base or factor == None:
        return False
    
def check_for_factor(base, factor):
    return base % factor == 0

"""Write function RemoveExclamationMarks which removes all exclamation marks from a given string."""
def remove_exclamation_marks(s: str):
    return s.replace("!", "")

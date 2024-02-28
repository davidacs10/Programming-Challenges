"""Trolls are attacking your comment section!
A common way to deal with this situation is to 
remove all of the vowels from the trolls' comments, 
neutralizing the threat.

Your task is to write a function that takes a 
string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" 
would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel."""

def disemvowel(string_: str):
    vowels = "aeiouAEIOU"
    return "".join(char for char in string_ if char not in vowels)

print(disemvowel("This website is for losers LOL!"))


"""Given an integral number, determine if it's a square number"""

def is_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    raiz = n ** 0.5
    return raiz.is_integer()

print(is_square(25))

def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0

print(is_square(25))

"""Your classmates asked you to copy some paperwork for them. 
You know that there are 'n' classmates and the paperwork has 'm' pages.
Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0."""

def paperwork(n, m):
    if n <= 0 or m <= 0:
        return 0
    else:
        return n * m
    
print(paperwork(-5, 5))

"""Write a function named setAlarm/set_alarm/set-alarm/setalarm 
(depending on language) which receives two parameters. The first 
parameter, employed, is true whenever you are employed and the second 
parameter, vacation is true whenever you are on vacation.

The function should return true if you are employed and not 
on vacation (because these are the circumstances under which 
you need to set an alarm). It should return false otherwise. Examples:

employed | vacation 
true     | true     => false
true     | false    => true
false    | true     => false
false    | false    => false"""

def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    else:
        return False

print(set_alarm(True, False))

def set_alarm(employed, vacation):
    return employed and not vacation

print(set_alarm(False, False))

"""Your task is to make two functions ( max and min, or maximum and minimum, 
etc., depending on the language ) that receive a list of integers as input,
and return the largest and lowest number in that list, respectively.

* [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
* [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
* [42, 54, 65, 87, 0]             -> min = 0, max = 87
* [5]                             -> min = 5, max = 5
"""
def minimum(arr):
    if len(arr) != 0:
        return min(arr)

def maximum(arr):
    if len(arr) != 0:
        return max(arr)

print(minimum([]))

"""Given an array of integers as strings and numbers, 
return the sum of the array values as if all were numbers.

Return your answer as a number."""

def sum_mix(arr):
    return sum(int(num) for num in arr)

print(sum_mix([9, 3, '7', '3']))

def sum_mix(arr):
    return sum(map(int, arr))

print(sum_mix([9, 3, '7', '3']))

"""Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'"""

def solution(string):
    return string[::-1]

print(solution("world"))

"""In this kata you will create a function that takes a list of non-negative 
integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""

def filter_list(l):
    only_numbers = []
    for n in l:
        if isinstance(n, int):
            only_numbers.append(n)
    return only_numbers

l = [1,2,'a','b']
print(filter_list(l))

def filter_list(l):
  return [i for i in l if not isinstance(i, str)]

print(filter_list(l))

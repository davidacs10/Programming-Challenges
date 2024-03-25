"""The main idea is to count all the occurring characters in a string. 
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}."""


def count(s: str):
    letter = {}
    for i in s:
        if i in letter:
            letter[i] += 1
        elif len(s) == 0:
            return {}
        else:
            letter[i] = 1
    return letter


print(count(""))

from collections import Counter


def count(string):
    return Counter(string)


"""This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z."""


def accum(st):
    parts = []
    for i, c in enumerate(st):
        parts.append((c.upper() + c.lower() * i))

    return "-".join(parts)


print(accum("abcd"))


def accum(s):
    return "-".join(c.upper() + c.lower() * i for i, c in enumerate(s))


"""Given a string, you have to return a string in which each 
character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  """


def double_char(s: str):
    return "".join(i * 2 for i in s)


print(double_char("String"))

"""You will be given an array a and a value x. 
All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not."""


def check(a, x):
    return x in a


print(check(["t", "e", "s", "t"], "e"))

"""In this simple Kata your task is to create a function that 
turns a string into a Mexican Wave. You will be passed a string 
and you must return that string in an array where an uppercase letter is a person standing up. 

Rules
 1.  The input string will always be lower case but maybe empty.

 2.  If the character in the string is whitespace then pass over it as if it was an empty seat"""


def wave(people: str):
    wave_list = []
    for i, char in enumerate(people):
        if char.isspace():
            continue

        waves = people[:i] + char.upper() + people[i + 1 :]
        wave_list.append(waves)
    return wave_list


print(wave("string"))


def wave(str):
    return [
        str[:i] + str[i].upper() + str[i + 1 :]
        for i in range(len(str))
        if str[i].isalpha()
    ]


print(wave("Hola"))

"""Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times."""


def find_it(seq):
    counter = Counter(seq)
    for k, v in counter.items():
        if v % 2 != 0:
            return k


def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]


def find_it(seq):
    return [k for k, v in Counter(seq).items() if v % 2 != 0][0]


print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))


def findDuplicates(nums):
    frecuency = Counter(nums)
    twice = []
    for k, v in frecuency.items():
        if v == 2:
            twice.append(k)
    return twice


print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))

"""Check to see if a string has the same amount of 'x's and 'o's. 
The method must return a boolean and be case insensitive. 
The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false"""

def xo(s):
    s = s.lower()
    return s.count("x") == s.count("o")

"""Write a function to split a string and convert it into an array of words.

Examples (Input ==> Output):
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]"""

def string_to_array(s):
    if len(s) == 0:
        return [""]
    return s.split()

print(string_to_array("I love arrays they are my favorite"))

def string_to_array(string):
    return string.split(" ")

print(string_to_array("I love arrays they are my favorite"))
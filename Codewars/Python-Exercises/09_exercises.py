"""Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"
Names given are always valid strings."""

def are_you_playing_banjo(name: str):
    if name.startswith("R") or name.startswith("r"):
        return f"{name} plays banjo"
    return f"{name} does not play banjo"

print(are_you_playing_banjo("Rikki"))

"""An isogram is a word that has no repeating letters, 
consecutive or non-consecutive. Implement a function that 
determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true 
"aba" --> false 
"moOse" --> false (ignore letter case)"""

def is_isogram(string: str):
    isogram = {x.lower() for x in string}
    if len(isogram) == len(string) or len(isogram) == 0:
        return True
    return False
    

print(is_isogram("Dermatoglyphics"))

def is_isogram(string):
    return len(string) == len(set(string.lower()))

print(is_isogram("Dermatoglyphics"))

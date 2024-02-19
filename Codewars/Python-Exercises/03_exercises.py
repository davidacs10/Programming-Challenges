"""Complete the solution so that it returns true if the first
argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false"""

def solution(text, ending):
    return text.endswith(ending)


print(solution("sumo", "omo"))

"""ATM machines allow 4 or 6 digit PIN codes and PIN codes 
cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false"""

def validate_pin(pin):
    return pin.isdigit() and len(pin) == 4 or pin.isdigit() and len(pin) == 6

print(validate_pin("222222"))

def validate_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()

print(validate_pin("222222"))

"""Very simple, given a number (integer / decimal / both depending on the language), 
find its opposite (additive inverse).

Examples:

1: -1
14: -14
-34: 34"""

def opposite(number):
    return -number
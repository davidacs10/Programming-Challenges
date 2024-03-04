"""Write a function that takes an array of words and smashes 
them together into a sentence and returns the sentence. 
You can ignore any need to sanitize words or add punctuation, 
but you should add spaces between each word. 
Be careful, there shouldn't be a space at the 
beginning or the end of the sentence!

Example
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'"""
words = ['hello', 'world', 'this', 'is', 'great']
def smash(words):
    return " ".join(words)

print(smash(words))

"""Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.

Examples (input --> output)
4 --> 3 // we have 3 divisors - 1, 2 and 4
5 --> 2 // we have 2 divisors - 1 and 5
12 --> 6 // we have 6 divisors - 1, 2, 3, 4, 6 and 12
30 --> 8 // we have 8 divisors - 1, 2, 3, 5, 6, 10, 15 and 30"""
def divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i * i != n:
                count += 1
    return count

print(divisors(30))

def divisors(n):
    return  len([l_div for l_div in range(1, n + 1) if n % l_div == 0])
print(divisors(30))
"""
Create a function with two arguments that will return an array of the first n multiples of x.
Assume both the given number and the number of times to count will be positive numbers greater than 0.
Return the results as an array or list ( depending on language ).
"""
def count_by(x, n):
    numbers = []
    if x and n > 0:
        for i in range(1, n + 1):
            result = x * i
            numbers.append(result)
        return numbers
        
print(count_by(50, 5))

"""Deoxyribonucleic acid, DNA is the primary information storage 
molecule in biological systems. It is composed of four nucleic acid 
bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

Ribonucleic acid, RNA, is the primary messenger molecule in cells. 
RNA differs slightly from DNA its chemical structure and contains no Thymine. 
In RNA Thymine is replaced by another nucleic acid Uracil ('U').

Create a function which translates a given DNA string into RNA.
For example:

"GCAT"  =>  "GCAU"
The input string can be of arbitrary length - in particular, it may be empty.
All input is guaranteed to be valid, i.e. each input string will only ever 
consist of 'G', 'C', 'A' and/or 'T'."""

def dna_to_rna(dna: str):
    dna = dna.replace("T"[-1], "U")
    return dna
print(dna_to_rna("GCAT"))

"""Convert number to reversed array of digits
Given a random non-negative number, you have to return the 
digits of this number within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]"""

def digitize(n):
    number_list = []
    for i in str(n):
        number_list.append(int(i))
    number_list.reverse()
    return number_list

print(digitize(984764738))

def digitize(n):
    return [int(x) for x in str(n)[::-1]]

print(digitize(35231))




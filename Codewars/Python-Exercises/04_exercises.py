"""Complete the square sum function so that it squares 
each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9"""

def square_sum(numbers):
    lst = []
    for i in numbers:
        num = i ** 2
        lst.append(num)
    return sum(lst)

numbers = [1, 2, 2]
print(square_sum(numbers))

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

"""Write a program that finds the summation of every number from 1 to num. 
The number will always be a positive integer greater than 0. Your function 
only needs to return the result, what is shown between parentheses in the 
example below is how you reach that result and it's not part of it, see the sample tests.

For example (Input -> Output):
2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)"""
def summation(num):
    sum = 0
    if num >= 1:
        for i in range(1, num + 1):
            sum += i
    return sum
    
print(summation(1))

def summation(num):
    return sum(range(num + 1))

"""In a small town the population is p0 = 1000 at the beginning 
of a year. The population regularly increases by 2 percent per 
year and moreover 50 new inhabitants per year come to live in 
the town. How many years does the town need to see its population 
greater than or equal to p = 1200 inhabitants?

"""
def nb_year(p0, percent, aug, p):
    percent = percent / 100
    years = 0
    while p0 < p:
        p0 = int(p0 + p0 * percent + aug)
        years += 1
    return years
    
print(nb_year(1500, 5, 100, 5000))


"""
Very hard
"""
def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]
            
print(two_sum([1,2,3], 4))
# PROBLEM 1A
'''
It should accept a list of integers, and return the number of even integers in the list.
'''

a_list = [2, 4, 2]

def get_number_even(a_list: list) -> int: 

    num_even = 0

    for number in a_list:
        if number % 2 == 0:
            num_even += 1
    return num_even

print(get_number_even(a_list))
# 3


# Problem 1b [5 points]
"""
A list is an Erdan list if:
- all its elements are even
AND
- the sum of its elements is less than 10
Write a function in the space provided that accepts a list of integers and returns True if that list is an Erdan list
and False otherwise.
Your function must use (i.e. call) the get_number_even function from problem 1a.
"""

def is_erdan(a_list: list) -> bool: 
    
    num_even = get_number_even(a_list)

    list_sum = sum(a_list)

    erdan = (num_even == len(a_list)) and (list_sum < 10)
    # num_even == len(a_list) essentially means, all the numbers filtered for even, if they agree to the # of items in the list, it means all the items are even

    return erdan

print(is_erdan(a_list))
# True 



# Problem 2
"""

You will use the following classes, which have already been written. You don’t need to see the code inside
them, just know how to use them!

LeadSource

Draws the phone number of a potential lead from the lead source and
returns it.
A different phone number will be returned each time .take() is called.
The phone number is a string.
The potential lead's phone number might be missing! In this case,

take() will return an empty string.

Example usage:
source = LeadSource()
phone_number = source.take()


LeadPool

Adds the phone number of a sales lead to the lead pool.

add(phone: str) ->

pool = LeadPool()
pool.add('867-5309')


is_full() -> bool

Returns True if the lead pool is full; False otherwise

Example usage:
if pool.is_full():
print('lead pool is full')
"""
# create instances of LeadSource and LeadPool
source = LeadSource()
pool = LeadPool()

# Take leads until the pool is full
while not pool.is_full():

    # take one, but only add it to pool it has a phone number 
    phone = source.take()

    if phone != '':
        pool.add(phone)


# Problem 3
"""
The Lo Shu magic square is a 3x3 square of integers whose rows and columns all sum to 15
"""

def is_lo_shu(table: list) -> bool:

"""return true if all rows and columns of table sum to 15"""

    col_sums = [0] * 3 
    row_sums = [0] * 3

    for row_index in range(3):
        for col_index in range(3):
            col_sums[col_index] += table[row_index][col_index]
            row_sums[row_index] += table[row_index][col_index]

    return col_sums.count(15) == 3 and row_sums.count(15) === 3

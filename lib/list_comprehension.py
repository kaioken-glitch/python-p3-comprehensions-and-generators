#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]

## list comprehension syntax:
# squared_minus_one = [(n **2) - 1 for n in range(1, 11)]
# new_list = [optional_operation(item) for item in old_list if optional_condition == True]

# one_to_three = range(1,4)

# a list comprehension that squares each number in one_to_three
# and assigns it to squared_lc
# squared_lc = [n ** 2 for n in one_to_three]

# a generator expression that squares each number in one_to_three
# and assigns it to squared_ge
# squared_ge = (n ** 2 for n in one_to_three)

# Looping through each shows identical values...
# for n in squared_lc:
#     print(n)
# 
# for n in squared_ge:
#     print(n)

# But the objects are NOT identical
# print(squared_lc)
# [1, 4, 9]
# print(squared_ge)
# <generator object <genexpr>>

# generator expressions are lazy, so they do not compute instead they return a generator object that can be iterated over later

# import sys 
# 
# lst_comp = [n for n in range(100000)]
# gen_exp = (n for n in range(100000))
# 
# sys.getsizeof(lst_comp)  # This will return the size of the list in bytes
# sys.getsizeof(gen_exp)   # This will return the size of the generator in bytes
# -*- coding: utf-8 -*-
"""
Problem: given a number, find the prime factors of the number and print them in a list

@author: john.pavlovich
"""

def get_prime_factors(u_input):
    factor_list, x = [], 2
    while x <= u_input:
        if (u_input % x) == 0:
            factor_list.append(x)
            u_input = u_input / x
        else:
            x = x + 1
    return factor_list
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 13:54:29 2021

@author: john.pavlovich
"""

import re

def is_palindrome(user_input):
    normal = ''.join(re.findall(r'[a-z]+', user_input.lower()))
    reverse = normal[::-1]
    return normal==reverse
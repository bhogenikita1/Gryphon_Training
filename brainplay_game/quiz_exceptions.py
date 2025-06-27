# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 11:01:10 2025

@author: HP
"""

def safe_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❗ Invalid input. Please enter a valid number.")

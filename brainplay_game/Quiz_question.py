# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 11:00:17 2025

@author: HP
"""
import random
import math

def generate_question():
    question_type = random.choice(["square", "square_root"])

    if question_type == "square":
        number = random.randint(1, 100)
        question = f"What is the square of {number}?"
        answer = number ** 2
    else:
        root = random.randint(1, 100)
        number = root ** 2
        question = f"What is the square root of {number}?"
        answer = root

    return question, answer

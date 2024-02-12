# Homework 13p1 Python Repitition 
# File: HW13p1_Task2_may2am.py 
# Date:    27 11 2023
# By:      Alex May
# Section: 001
# Team:    007
# 
# ELECTRONIC SIGNATURE
# Alex May
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# This code will test a random number for the BPS catagories and it will repeat this the amount of times a user inputs

#import libraries
import math
import random

#Ask user for input
n = int(input("Enter the number of readings: "))

#establish outputs
hyper = 0
hypo = 0
normal = 0

for k in range(n):
    flip = random.randint(65,140)
    if flip < 90 and flip >= 50:
        hypo += 1
    if flip < 120 and flip >= 90:
        normal += 1
    if flip < 210 and flip >= 120:
        hyper += 1

#output
print("The amount of hypotension readings were", hypo)
print("The amount of normal readings were", normal)
print("The amount of hypertension readings were", hyper)




'''
Challenge 1: Greatest Common Divisor
------------------------------------
In this challenge, your task is to find the greatest common divisor of two numbers a and b.

Problem Statement
Write a findGCD function that takes in two numbers as input a and b and finds the greatest common divisor of the two.

Input
Two numbers

Output
GCD of numbers

Sample Input
a = 8, b = 12

Sample Output
4

'''

import math 
## Write your function here
def findGCD(a, b):
  
  return math.gcd(a, b)

print(findGCD(12,48))
'''
Challenge 9: Even Squares Not Divisible By Three

Problem Statement
------------------
Given a getSquare() function, make a list comprehension that returns a list with the 
squares of all even numbers from 0 to 20, but ignores those numbers that are divisible by 3.

Input
An empty list

Output
A list with the square of all even numbers not divisible by 3.

'''
def getSquare():
  ##Write your code here
  l1 = [x**2 for x in range(21) if x % 2 == 0 and x**3 % 3 != 0] ##Create the list here
  return l1
print(getSquare())
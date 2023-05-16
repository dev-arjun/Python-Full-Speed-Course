'''
Challenge 5: List of Squares

Problem Statement
Given a getSquare() function, create a list with the squares of the first 10 numbers, i.e., in the range from 1-10.

Input
An empty list

Output
An updated list with the square of each value in the list

'''

def getSquare():
  ## Write your code here
  l1 = [x**2 for x in range(1,11)] ## Create your list here
  return l1

print(getSquare())
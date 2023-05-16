'''
Challenge 6: List of Cubes

Problem Statement
Given a getCube() function, create a list with the cubes of the first 20 numbers.

Input
An empty list

Output
An updated list with the cube of each value in the list
'''

def getCube():
  ## Write your code here 
  l1 = [x*x*x for x in range(1,21)] ## Make the list here
  return l1

print(getCube())
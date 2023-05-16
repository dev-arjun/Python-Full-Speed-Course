"""
Problem Statement
Given an inRange(x,y) function, write a method that determines whether a given pair (x, y) falls in the range (x < 1/3 < y). 
Essentially, you’ll be implementing the body of a function that takes in two numbers x and y and returns True if x < 1/3 < y; otherwise, it returns False.


"""

"""
Input
Two numbers, x and y

Output
True if x and y are in the range and False otherwise.

Sample Input
x = 2, y = 3

Sample Output
False
"""

#Coding Exercise
def inRange(x, y):
  ## Write your code here
  if x < 1/3 < y:
    return True
  else:
    return False ## Change this to return True or return False depending on your output

print(inRange(5,10))

"""
def inRange(x, y):
  return (x < 1/3 < y)

print(inRange(-1, 3))
print(inRange(2, 3))

"""
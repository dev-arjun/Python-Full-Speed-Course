'''
Challenge 7: Lists of Even and Odd Numbers

Problem Statement
Given a ListofEvenOdds() function, create a list comprehension with all the even numbers from 0 to 20, and another one with all the odd numbers.

Input
Two empty lists

Output
List 1 with even numbers

List 2 with odd numbers

Coding Exercise
You have been given some starter code and a return statement that allows 
you to return the lists you create.
'''

def ListofEvenOdds():
  l1 = [x for x in range(21) if x%2==0] # list of even numbers
  l2 = [x for x in range(21) if x%2==1] # list of odd numbers 
  return [l1, l2]

print(ListofEvenOdds())
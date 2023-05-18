'''
Challenge 4: Increment Dictionary Values

Problem Statement
Implement an updateAges function that receives ages dictionary and a number n and returns a new dictionary where each student is (n) years older.

Input
A dictionary

Output
Returns a copy of sorted ages where each student is n years older.


'''
def updateAges(ages, n):
  new_ages = {}
  for word in ages:
    new_ages[word] = ages[word] + n
  return new_ages
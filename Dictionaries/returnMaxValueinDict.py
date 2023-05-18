'''
Challenge 3: Return Key With Maximum Value

Problem Statement
Implement an oldestStudent function that receives the ages dictionary as a parameter, and returns the name of the oldest student.

Input
A dictionary

Output
The key associated with highest age, i.e., the name of the oldest student

'''

def oldestStudent(ages):
  values = list(ages.values())
  keys = list(ages.keys())
  return keys[values.index(max(values))]
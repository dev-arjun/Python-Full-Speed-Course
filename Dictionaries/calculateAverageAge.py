'''
Challenge 6: Average Values Within Multiple Dictionaries

Problem Statement
Implement a calculateAverageAge function that receives the students dictionary and returns the average age.

Input
A nested dictionary

Output
The average age of students

'''

def calculateAverageAge(students):
  sumofval = 0
  length = len(students.keys())
  for ages in students.values():
    age = ages['age']
    sumofval += age
  return sumofval/length
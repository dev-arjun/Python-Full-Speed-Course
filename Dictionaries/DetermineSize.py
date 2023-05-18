'''
Challenge 1: Determine Size of a Dictionary


Problem Statement#
Given a lengthDictionary function that takes Students dictionary as a parameter, find how many students are in the dictionary.

Input
A dictionary

Output
The size of the dictionary

'''
def calculateAverageAge(students):
  sumofval = 0
  length = len(students.keys())
  for ages in students.values():
    age = ages['age']
    sumofval += age
  return sumofval/length
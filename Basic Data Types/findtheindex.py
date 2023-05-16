"""
Challenge 5: Find Index of a Specific Value in a String
"""

"""
Problem Statement:

Given a string, use a findOccurence(s) function that allows you to find the first
occurrences of "b" and "ccc"​ in the string.

"""

"""
Input
-------------
A string

Output
-------------
The first occurrence of “b” and “ccc” in the string

Sample Input
-------------
aaabbbccc

Sample Output
-------------
[3, 6]

"""

#Coding Exercise
def findOccurence(s):
  a = s.find('b')#find first occurrence of "b" in the string 
  b = s.find('c')#find first occurence  of "ccc" in the string
  return [a, b]

print(findOccurence("test of b and c"))
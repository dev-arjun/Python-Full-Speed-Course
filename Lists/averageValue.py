"""
Challenge 3: Averaging Values in a List

Problem Statement
Given a getAverage() function, create a list named l with the following values:

[1, 4, 9, 10, 23]

Calculate the average value of all values in the list.

Input
---------
A list of integers

Output
---------
An average of values in the list

Sample Input
-------------
[1, 4, 9, 10, 23]

Sample Output
-------------
9.4

"""

def getAverage():
  l1 = [1, 4, 9, 10, 23]
  ## Write your code here
  avg = 0 
  for i in l1:
    avg += i
  avg = avg/len(l1)
  return avg

print(getAverage())
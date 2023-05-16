#lists is the data structures that group swquence of elements.
#lists can have elements of several datatypes


"""

Problem Statement
Given a getSublist() function, create a list named l [1, 4, 9, 10, 23]. Using list slicing, get the sublists [1, 4, 9] and [10, 23].

Input
-----
A list

Output
------
Two sublists

"""
#Coding Exercise
def getSubList():
  l = [1, 4, 9, 10, 23]
  l1 = l[0:3]
  l2 = l[3:5] ## Write your code here 
  return [l1, l2]  ## Alter the return statement to return your sublists


print(getSubList())


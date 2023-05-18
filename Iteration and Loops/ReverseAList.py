'''
Challenge 3: Reverse a List
In this challenge, your task is to reverse the elements in a list.

Problem Statement
Implement a reverse function that receives a list as a parameter and returns the reverse of that list. You may create an empty list and keep adding the values in reversed order as they come from the original list.

Input
A list

Output
The reverse of a list

Sample Input
[1, 2, 3, 4, 5]

Sample Output
[5, 4, 3, 2, 1]

'''


def reverse(list1):
  new_list = []
  for x in list1:
    new_list.insert(0,x)
  return new_list

print(reverse([1,2,3,4,5]))
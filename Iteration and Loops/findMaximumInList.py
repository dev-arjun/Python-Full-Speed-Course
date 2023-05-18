'''
Challenge 2: Find Maximum in a List

Problem Statement 1
Create a findMaximum function that receives a list as a parameter and returns the maximum value in the list. As you iterate over the list, you may want to keep track of the current maximum value in order to keep comparing it with the next elements of the list.

Input
A list

Output
Maximum number in the list

Sample Input
[1, 4, 9, 10, 23]

Sample Output#
max = 23

'''
#Coding Exercise
#-----------------#

def findMaximum(list):
    max = list[0]
    for x in list:
      if x > max:
          max = x
    return max
print(findMaximum([1,2,3,4,5,6]))

'''
Problem Statement 2

Modify the previous findMaximumValueIndex(list) function such that it returns a list with the first element being the index of the maximum value in the list and
the second being the maximum value. Besides keeping the maximum value found so far, you also need to keep the position where it occurred.

Input
A list

Output
Maximum number and index of the number in the list

Sample Input
[1, 4, 23, 10, 9]

Sample Output
max = 23

index = 2

'''

def findMaximumValueIndex(list):
    maximum = list[0]
    for index , number in enumerate(list):
      if number > maximum:
          maximum = number
    return [index, number]

print(findMaximumValueIndex([1,2,3,4,5,6]))
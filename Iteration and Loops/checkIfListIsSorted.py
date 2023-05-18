'''

Problem Statement
------------------
Make an isSorted function that receives a list as a ​parameter and returns true if the list is sorted in ascending order.

For instance, [1, 2, 2, 3] is ordered while [1, 2, 3, 2] is not.

Input
------
A list

Output
------
True if the list is sorted and False otherwise


'''

def isSorted(list):
  flag = 0
  i = 1
  while i < len(list): 
      if(list[i] < list[i - 1]): # compare with the previous element
          flag = 1
      i += 1
      
  if (not flag) : 
      return True 
  else : 
      return False 

print(isSorted([2,7,6,1,7]))
print(isSorted([1,2,3,4,5]))
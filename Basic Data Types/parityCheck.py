#Parity is a term to express if a given integer is even or odd
'''
Given a checkParity(n) function, write code to determine if a given number n is even or odd.
Think of this as a function that returns 0 if the number is even, and 1 if it is odd.
You have been given some starter code where the function and return statement have already been written,
so don’t worry about any Python-specific details about functions;
just implement the function logic!

'''

'''
Input
-----------
A number

Output
------------
The parity of the number


Sample Input
4

Sample Output
0

'''

def checkParity(n):
  #Mycode
  if n % 2 == 0:
    result = 0 #updating the value of result as 1, if the result is even
  else:
    result = 1 #updating the value of result as 1, if the result is odd
  return result

print(checkParity(5))
print(checkParity(6))
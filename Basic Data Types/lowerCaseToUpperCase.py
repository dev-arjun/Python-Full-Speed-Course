#Challenge 6: Lowercase to Uppercase

"""
Problem Statement
Given a function changeCase(s), the task is to convert the strings from upper case to lower case.

Input
A string in upper case

Output
Change case of the string in lower case

Sample Input
“AAA BBB CCC”

Sample Output
“aaa bbb ccc”

"""

#Coding Exercise#
def changeCase(s):
  a = s.upper() # convert string to "AAA BBB CCC"
  b = s.lower() # convert string to "aaa bbb ccc"
  return [a, b]

print(changeCase("This is a sample text case"))
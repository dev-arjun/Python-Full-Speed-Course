"""
List comprehensions can be used to create lists based on conditions applied 
to elements of an existing list.

Syntax

--------------------------------------------------------------------------------------------------------------------------------------------
Output Expression for variable in reference sqence if condition(optional) else "Output for Else" for variable in reference sqence optional)
--------------------------------------------------------------------------------------------------------------------------------------------

Sample Code with If condition:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

"""
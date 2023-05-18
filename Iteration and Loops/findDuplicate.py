'''
Challenge 5: Find Duplicates in a List

Problem Statement
Implement the hasDuplicates function which verifies if a list has duplicate values.

Input
A list

Output
True if the list has duplicates and False otherwise

'''
def hasDuplicates(list):
    flag = 0
    for x in range(len(list)):
        for y in range(x+1, len(list)):
            if (list[x] == list[y]):
                flag = 1

    if (flag == 1) : 
        return True 
    else : 
        return False 


print(hasDuplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(hasDuplicates([1, 2, 3, 1, 5]))
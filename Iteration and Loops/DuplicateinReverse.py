'''
Challenge 6: Print Even/Odd Numbers in Descending Order

Problem Statement
Implement a printEvenOdd function that receives a number n as parameter and prints–in decreasing order–which numbers are even and which are odd until it reaches 0. For instance, on calling printEvenOdd(10) it prints

Input#
The input will be a number n. We have used n = 10 in the below output.

Output#
        Even number: 10
        Odd number: 9
        Even number: 8
        Odd number: 7
        Even number: 6
        Odd number: 5
        Even number: 4
        Odd number: 3
        Even number: 2
        Odd number: 1


'''

def printEvenOdd(n):
    for x in range(n, 0,-1):
        if x % 2 == 0:
            print("Even number:", x)
        else:
            print("Odd number:", x)

printEvenOdd(10)
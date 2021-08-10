"""

Problem Statement
Excel is a very successful Microsoft product, used by billions of people around the world. A common problem our customers are facing is that they create Excel sheets which cannot be correctly evaluated. We want to create a "spell checker" to reduce these errors.
A simple Excel sheet contains columns AA to ZZ and rows between 00 to 99. For example, AA00 is the top-left cell and MN54 is approximately in the middle.
Each cell contains rational numbers or a mathematical expression, potentially referencing other cells. An empty cell can be assumed to contain the number 0.
An Excel sheet can be evaluated if it is possible to deterministically expand all mathematical expressions to rational numbers.
For example:
This Excel sheet can be evaluated:

.   AA  AB  AC
00  10  15
01  AA00 + AB00

This Excel sheet cannot be evaluated:

.   AA  AB  AC
00  10  (AA00 + AA01) * 15
01  20 + AB00



You are given an Excel sheet. Write a program which will determine if it can be evaluated.
Input Data
The data is given as a list of cells and values (either as an array of strings or from a file), in random order:
Example 1
AA00 = 10
AA01 = AA00 + AB00
AB00 = 15
Your program will output:
The Excel sheet can be evaluated.

Example 2
AA00 = 10
AB00 = (AA00 + AA01) * 15
AA01 = 20 + AB00
Your program will output:
The Excel sheet cannot be evaluated.

Follow-up Question 1
The mathematical operations, possibly grouped by parentheses ( and ), are:
Addition +Subtraction -Multiplication *Division /Unary -
The standard operator precedence applies.
Write a program to determine, for each cell, whether the mathematical expression is correct. For example, for the expression:
AB00 = (AA00 + AA01) * 15)
Your program will display:
AB00: Incorrect expression
Follow-up Question 2
If the Excel sheet can be evaluated, and the mathematical expressions are correct, your program will evaluate the expressions and display the resulting data in each cell.
For Example 1, your program will output:
AA00 = 10
AB00 = 15
AA01 = 25
"""

import re


def read_file(strs) -> dict:
    dct = {}
    for i in strs:
        l, r = i.replace(' ', '').split('=')
        r = re.findall(r'[A-Z]{2}\d{2}', r)
        dct[l] = r
    return dct


def has_cycle(graph):
    visited = set()
    for i in graph:
        if i in visited:
            continue
        stack = [i]
        visited_in_round = {i}
        while stack:
            cur = stack.pop()
            for j in graph[cur]:
                if j in visited_in_round:
                    return True
                visited_in_round.add(j)
                visited.add(j)
                stack.append(j)
    return False


if __name__ == '__main__':
    strs = ['AA00 = 10', 'AA01 = AA00 + AB00', 'AB00 = 15']
    g = read_file(strs)
    print(has_cycle(g))

    # 1. Read file by line, split by '=' and other operators, obtain a dependency graph in the form of a dictionary
    # 2. Detect if there are cycles in the dependency graph, if yes, it suggests the values of Excel cells cannot be evaluated

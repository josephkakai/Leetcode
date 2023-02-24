#!/usr/bin/python
"""soln to the 2 sun problem"""

def twosum(list, target):
    #outer loop of the soln
    for a in range(len(list)):
        #inner loop that enables the subsequent additions
        for b in range(a + 1, len(list)):
            sum = list[a] + list[b]
            if sum == target:
                return (a, b)


list = [4, 5, 1, 3]
target = 6
print(twosum(list, target))

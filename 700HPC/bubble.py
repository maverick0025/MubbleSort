import time

def bubble_sort(Array):

    n = len(Array)
    for i in range(n-1):
        flag = True
        for j in range(n-i-1):
            if Array[j] > Array[j+1]:
                flag = False
                Array[j], Array[j+1] = Array[j+1], Array[j]
        if flag:
            break   
    return Array

'''
Time Complexity: O(n^2)
Space Complexity: O(1)
'''
"""I'm new to coding and now I want to get the sum of two arrays...actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.
"""
def array_plus_array(arr1,arr2):
    x = 0
    for i in range(0, len(arr1)):
        x += arr1[i]
    for i in range (0, len(arr2)):
        x+= arr2[i]
#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Shaun Jullens
# Finds max or min of an array

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def minV(arr):
    return min(arr)

def maxV(arr):
    return max(arr)

if __name__ == "__main__":
    print("Array: ", arr)
    print("Min element of array: ", minV(arr))
    print("Max element of array: ", maxV(arr))


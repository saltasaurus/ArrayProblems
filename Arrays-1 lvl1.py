#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Shaun Jullens
# This code finds if a value x is in all k sized segments in an array

def findx(arr, k, x):
    n = len(arr)
    
    for i in range(0,n,k):
        if (x in arr[i:i+k]):
            found = True
        else:
            found = False
            break
    return found

if __name__ == "__main__":
    arr = [ 3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3 ] 
    x, k = 3, 3
    
    #arr = [21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25]
    #x, k = 23, 5 

    #arr = [5, 8, 7, 12, 14, 3, 9]
    #x, k = 8, 1
    
    #arr = [1, 2, 1, 2, 1, 2, 1]
    #x, k = 1, 2
    
    if (findx(arr, k, x)): 
        print("Yes") 
    else : 
        print("No") 


# In[ ]:





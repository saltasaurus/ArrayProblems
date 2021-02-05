# Shaun Jullens
# Sorting an array
# Selection, Binary, Merge, Radix, Insertion, Quick

# Swaps two values in an array
def swap(arr, p1, p2):
    arr[p1], arr[p2] = arr[p2], arr[p1]
    return arr

# Sort by looping through 
def SelectionSort(arr):
    l = len(arr)
    # Loop through entire array
    for i in range(l):
        minv = i
        # Loop through unsorted array 
        for ii in range(i+1,l):
            # Find min in unsorted array
            if (arr[minv] > arr[ii]):
                minv = ii
        arr = swap(arr, i, minv)
    return arr

# Helper function for MergeSort
def merge(arr, mid):
    left = arr[:mid]
    right = arr[mid:]

    left_idx = right_idx = sort = 0
    while(left_idx < len(left) and right_idx < len(right)):
        if (left[left_idx] <= right[right_idx]):
            arr[sort] = left[left_idx]
            left_idx = left_idx + 1
        else:
            arr[sort] = right[right_idx]
            right_idx = right_idx + 1
        sort = sort + 1

    while left_idx < len(left):
        arr[sort] = left[left_idx]
        left_idx = left_idx + 1
        sort = sort + 1
    
    while right_idx < len(right):
        arr[sort] = right[right_idx]
        right_idx = right_idx + 1
        sort = sort + 1

    return arr

# Sort by recursively splitting an array and sorting pieces 
def MergeSort(arr):
    mid = len(arr)//2
    if len(arr) > 1:
        # Find middle of array
        # Recursively sort left-split array
        MergeSort(arr[:mid])
        # Recursively sort right-split array
        MergeSort(arr[mid:])
        
    return merge(arr, mid)

if __name__ == "__main__":
    
    array = [38, 27, 43, 3, 9, 82, 10]
    array = [3, 5, 23, 24, 62, 63, 16, 16, 16, 1]
    print("Selection Sort: ", SelectionSort(array))
    print("Merge Sort: ", MergeSort(array))
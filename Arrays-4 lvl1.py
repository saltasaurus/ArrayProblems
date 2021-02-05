# Shaun Jullens
# Sorting an array
# Selection, Binary, Merge, Radix, Insertion, Quick


def swap(arr, p1, p2):
    arr[p1], arr[p2] = arr[p2], arr[p1]
    return arr

def SelectionSort(arr):
    l = len(arr)
    for i in range(l):
        minv = i
        for ii in range(i+1,l):
            if (arr[minv] > arr[ii]):
                minv = ii
        arr = swap(arr, i, minv)
    return arr

# def MergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         print(mid)
#     return arr

if __name__ == "__main__":
    
    array = [38, 27, 43, 3, 9, 82, 10]
    
    print(SelectionSort(array))
    #print(MergeSort(array))
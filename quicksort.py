# Quicksort algorithum example from Grokking

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]

        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


print("Quicksort of [3, 5, 21, 9, 1]: ", quicksort([3,5,21,9,1]))
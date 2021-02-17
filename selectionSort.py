#Selection Sort
# Sort a list of items from smalles to largest

# O(n2) run time

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def SelectionSort(arr):
    newArr = []
    for j in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(range(5))

print(SelectionSort([3,9,7,2,8]))
# A function that finds the sum of an array with recursion

def RSum(arr):
    if arr == []:
        return 0
    return arr[0] + RSum(arr[1:])

print("Sum of [3, 5, 4] array is: ", RSum([3,5,4]),"\n")


def listLen(arr):
    if arr == []:
        return 0
    return 1 + listLen(arr[1:])

print("Length of [3, 5, 4] array is: ", listLen([3,5,4]),"\n")

# Max list recursively, Derived answer from whiteboarding
def listMax(arr):
    if arr == []:
        print("Invalid input")
        exit()
    if len(arr) == 1:
        return arr[0]
    if len(arr) > 1:
        max = listMax(arr[1:])
        if arr[0] < max:
            return max
        else:
            return arr[0]

# Recursive Max list from Grokking
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print("Max value of [3,5,4] array is: ", listMax([3,5,4]), "\n")


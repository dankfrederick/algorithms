#Binary Search

#Used for ordered lists or arrays with a running time of Log2 N (2^10 = n of 1024, or 10 guesses to fine the correct answer in a pool of 1024 choices)

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,3,5,7,9]
item = 3

print("Position of value: ", item, " is: ",binary_search(my_list,item))



# number of guesses required

#128 item list

import math

print(math.log(128,2))

# 7 gueeses

#256 item list = 8 guesses

#Running Time:
# O(n) = log time or O(log n)
# Demonstration of the Factorial Recursive Function

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print("3 Factorial: ",fact(3))

print("5 Factorial: ", fact(5))

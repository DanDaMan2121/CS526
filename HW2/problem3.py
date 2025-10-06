# Problem 3
# Consider the following funciton:
def doIt(n): 
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return doIt(n-1) + doIt(n-2) - doIt(n-3)
    
# Implement this function and output doIt(1), doIt(3), doIt(6)

print(doIt(1))
print(doIt(2))
print(doIt(3))
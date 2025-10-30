# fileName = './testRightAngle/rightangles_3.txt'
fileName = './testFewest/fewest_3.txt'
myList = []
t = 0
with open (fileName, 'r') as file:
    
    for i, line in enumerate(file):
        if i == 1:
            t = int(line)
        if i > 1:
            newLine = line.strip('\n')
            myList = newLine.split(' ')
intList = list(map(int, myList))

def smallest_number_elements(arr, T):
   # Sort array in descending order
    arr_sorted = sorted(arr, reverse=True)
    total = 0
    count = 0
    for num in arr_sorted:
        total += num
        count += 1
        if total > T:
            return count
    return count  # fallback, sum(arr) > T guaranteed


count = smallest_number_elements(intList, t)
print(count)
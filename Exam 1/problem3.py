
fileName = './testShoppingCart/sc_input3.txt'
myList = []


with open (fileName, 'r') as file:
    
    for i, line in enumerate(file):
        if i > 0:
            newLine = line.strip('\n')
            myList.append(newLine)
myList = myList[0].split(',')
print(myList)

basket1 = []
basket2 = []
count = 0
switch = True
for e in myList:

    if not basket1:
        basket1.append(e)
    elif e == basket1[0]:
        basket1.append(e)
    elif e != basket1[0] and not basket2:
        basket2.append(e)
    elif e == basket2[0]:
        basket2.append(e)
    else: 
        if switch:
            basket1 = []
            basket1.append(e)
            switch = False
        else:
            basket2 = []
            basket2.append(e)
            switch = True
    
    tempVal = len(basket1) + len(basket2)
    if tempVal > count:
        count = tempVal

ans = (basket1, basket2)
print(count)
print(ans)
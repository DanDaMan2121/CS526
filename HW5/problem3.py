import sys

def longestSequence(A, B):
    m, n = len(A), len(B)
    dpA = [1] * m
    dpB = [1] * n

    for i in range(m):
        for j in range(n):
            # if A[i] can follow B[j]
            if B[j] < A[i]:
                dpA[i] = max(dpA[i], dpB[j] + 1)
            # if B[j] can follow A[i]
            if A[i] < B[j]:
                dpB[j] = max(dpB[j], dpA[i] + 1)

    return max(max(dpA), max(dpB))






if __name__ == '__main__':

    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        list1 = []
        list2 = []
        with open (fileName, 'r') as file:
            for i, line in enumerate(file):
                if i == 0:
                    size1 = int(line.strip('\n'))
                elif i == 1:
                    size2 = int(line.strip('\n'))
                elif i == 2:
                    newLine = line.strip('\n')
                    list1 = list(map(int, newLine.split(' ')))
                else:
                    newLine = line.strip('\n')
                    list2 = list(map(int, newLine.split(' ')))
                    
        if size1 < size2:
            size = size1
        else:
            size = size2
        # print(size)
        list3 = longestSequence(list1, list2)
        # print(len(list3))
        print(list3)
        

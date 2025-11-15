import sys


def longestSequence(A, B):
    m, n = len(A), len(B)
    dpA = [[a] for a in A]  # sequences ending at A[i]
    dpB = [[b] for b in B]  # sequences ending at B[j]

    for i in range(m):
        for j in range(n):
            if i == j:
                continue  # skip same index pairs

            # From B[j] to A[i] (must have j < i for subsequence order)
            if j < i and B[j] < A[i]:
                if len(dpB[j]) + 1 > len(dpA[i]):
                    dpA[i] = dpB[j] + [A[i]]

            # From A[i] to B[j] (must have i < j for subsequence order)
            if i < j and A[i] < B[j]:
                if len(dpA[i]) + 1 > len(dpB[j]):
                    dpB[j] = dpA[i] + [B[j]]

    # Pick the best sequence overall
    bestA = max(dpA, key=len, default=[])
    bestB = max(dpB, key=len, default=[])
    best = bestA if len(bestA) >= len(bestB) else bestB

    return best












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
                    
      
        sequences = longestSequence(list1, list2)
        # for s in sequences:
        #     print(s)
        print(f"Longest sequences: {len(sequences)}")

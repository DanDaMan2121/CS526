# Problem 4

# • A group of n Ghostbusters is battling n ghosts. Each Ghostbuster carries a proton pack which shoots a steam at a
#   ghost destroying it. A stream goes in a straight line in both directions and continues when it hits the ghost. The
#   Ghostbusters decide upon the following strategy:
# • They will pair off with the ghosts, forming n Ghostbuster-ghost pairs and then simultaneously each
#   Ghostbuster will shoot a stream at their chosen ghost. The streams are not allowed to cross so each
#   Ghostbuster must choose a paring for which no streams will cross.
# • You can assume that there are an equal number Ghostbusters and ghosts.
# • Create a solution which will determine if all of the Ghosts can be eliminated in a single shot of the Ghostbusters
#   by returning the string “All Ghosts: “ <were|were not> “ eliminated”
# • Partial credit will be given for the design and algorithm and full credit will be given for a correct working solution.
# • I will provide a set test cases in the format:
# • Line 1 will contain the number of Ghostbusters
# • Lines 2-n will contain a ghostbuster, ghost paring represented as a series of letters and numbers space separated with a B indicating the
#   position of a Ghostbuster, a G indicating the position of a ghost. The information following either a B or a G will be the X Y coordinate of
#   either the ghostbuster or the ghost.

import math
import os
class coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return ((self.x - other.x )/ (self.y - other.y))

# folderName = 'C:/Users/dbara/OneDrive/Desktop/CS526/HW3/testGhostbusters'
folderName = './testGhostbusters'
myAns = []
fileCount = 0
for fileInFolder in os.listdir(folderName):
    fileName = folderName + '/' + fileInFolder
    with open(fileName, 'r') as file:
        # Core of algorithm

        result = 'All Ghosts: were eliminated'
        slope = set()
        for line in file:
            indexB = line.find('B')
            indexG = line.find('G')
            indexEnd = line.find('\n')
            if indexB != -1:
                firstCoordLine = line[indexB + 2: indexG - 1]
                secondCoordLine = line[indexG + 2: indexEnd]
                
                firstCoord = firstCoordLine.split(' ')
                secondCoord = secondCoordLine.split(' ')

                buster = coordinate(int(firstCoord[0]), int(firstCoord[1]))
                ghost = coordinate(int(secondCoord[0]), int(secondCoord[1]))
                
                slope.add(buster - ghost)

                if len(slope) > 1:
                    result = 'All Ghosts: were not eliminated'
                    break

        # End of Algorithm 

        fileCount += 1
        # print(result)
        myAns.append(result)


# Compares your answers with another folder's

# ansFolderName = './ansGhostbusters'
# count = 0
# for fileInFolder in os.listdir(ansFolderName):
#     fileName = ansFolderName + '/' + fileInFolder
#     with open(fileName, 'r') as file:
#         for line in file:
#             newLine = line.strip('\n')
#             if newLine == myAns[count]:
#                 print(newLine, ' == ', myAns[count])
#             else:
#                 print(newLine, ' != ', myAns[count])
#             count += 1
    
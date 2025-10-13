## Problem 1
In problem 1 we are asked to determine if a string is a palindrom or not. This is simple. I iterated the from the start and from the end simultaneously checking to see wheather the current "head" was equal to the current "tail". If they were equal we could continue the iteratrion until until the index of the head surpassed the index of the tail. Indicating that we have iterated the whole string. If at any point the "head" did not equal the "tail" we know that that is not a palindrome and the function will end.

### DIRECTIONS: 
1. Call palindrome method with a string as an argument.

## Problem 2
In problem 2 we are tasked to generate all the unique substrings of a string. To get every unique substring was fairly simple for me. I decided to use a set, and add any substring to that set I would generate. This is because sets can only have unique values meaning duplicates will be disregarded. Now to generate every possible substring using recusion is a little trickyer. I came up with the idea to move the head of the substring by 1 then recall the my function. This generated some of the substrings I needed but not all. To achieve this I would call the function again immediately after moving the head. This time however, I would move the tail which would generate the rest of the possible substrings on the back from reaching the terminal condition. The terminal condition being if the head is equal to the tail return.


### DIRECTIONS
1. Call "generateAllSubStrings" method with a string as a argument, and an empty set.


## PROBLEM 3a
The "reverseArray" function reverses the stack by recursively popping all elements until the stack is empty. As the recursion returns, each popped element is inserted at the bottom of the stack using "insertBottomArray", which ensures the original top elements end up at the bottom, reversing the order.

### DIRECTIONS
1. Call "reverseArray" method with an arrayStack as an argument.

## Problem 3b & 3c
The reverseLinkedList method works by recursively removing the top element until the stack is empty. Then, as the recursion unwinds, it uses insertBottom to place each removed element at the bottom of the stack, effectively reversing the original order. Furthermore, becuase 3b and 3c's structures are so similar they can both use this function.

### DIRECTIONS:
1. Call "reverseLinkedList" method with a linkedListStack or doublyLinkedStack list as an argument.

## Problem 4
In problem 4 we are told that a ghostbuster shoots a stream at a ghost forming a line. There are multiple ghostBuster and for each ghostBuster there is a ghost. Lines formed by these ghost busters are prohibited from corssing. We are given the positions of each ghostBuster and ghost. From their position we can deduced the slope between each ghost and ghostBuster respectively. This is important because lines that are parallel or lines that share the same slope do not intersect. This is the core of my algorithm. I first created a data structure that stores the x and y values of the position of each ghost and ghostBuster respectively and then I calculated the slope between the ghostBuster and the ghost and added that value to a set. Sets can only have unique values so any duplicates are disregarded. I used a conditional statement that would break out of the loop checking the slope of every ghostBuster if the set's length became greater than 1. This is becuase if the set is greater than 1 that would mean that not all the slopes are parallel and therefore would intersect.

### DIRECTIONS: 
1. change the variable "folderName" to the reltive or absolute path of the folder that contains your tests. The path must be formated similar to the example I have above "folderName".
2. Run the scipt. 

?. I also have a variable called "myAns" which contains all of my answers in problem 4 if you would like to use that instead.

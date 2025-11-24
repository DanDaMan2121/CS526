## PROBLEM 1
Merge Sort: Merge sort works by dividing the list into two halves, recursively sorting each half, and then merging the two halves back together in sorted order.

Quick Sort: Quick Sort works by picking a pivot element from the list. It then splits the other elements into two groups, those less than or equal to the pivot and those greater than the pivot. The algorithm recursively sorts these two groups. Finally, it combines the sorted left group, the pivot, and the sorted right group into a new fully sorted list. This process repeats until all sublists are sorted and the entire list is in order

Insertion Sort: Insertion sort builds the sorted list one element at a time by taking each new element and inserting it into its correct position in the already sorted portion.

Merge sort has a guaranteed time complexity of O(n log n) for best, average, and worst cases, but it requires extra memory for merging. Quick sort has an average time complexity of O(n log n) but can degrade to O(n²) in the worst case; it uses less memory and is often faster in practice. Insertion sort has a worst-case time complexity of O(n²), but it is very efficient for small or nearly sorted lists, and it uses minimal memory. Merge sort is stable, quick sort is not stable, and insertion sort is stable. Merge sort is ideal for large datasets or external sorting, quick sort is best for large in-memory datasets, and insertion sort is suitable for small datasets or nearly sorted data.

DIRECTIONS: run the script while passing a test file as a command-line argument
ex: python .\problem1.py .\testSort\testSortinput1.txt


## PROBLEM 2
This code implements Radix Sort, a sorting algorithm that sorts numbers digit by digit, starting from the least significant digit. The currentExpSort function sorts the list based on a specific digit, determined by the exp. It counts how many times each digit occurs, computes the cumulative positions, and places the numbers into a new array in order based on that digit. The radixSort function first finds the largest number to determine how many digits need to be sorted. It then repeatedly calls currentExpSort for each digit, multiplying exp by 10 each time to move to the next digit. After all digit positions are processed, the list is fully sorted and printed.

Radix sort performance has a performance of O(n * k), where n is the number of elements and k is the number of digits; it can be faster than sorts like QuickSort or MergeSort for large datasets with small digit lengths. Use Radix Sort when you have integer.

DIRECTIONS: run the script while passing a test file as a command-line argument
ex: python .\problem2.py .\testRadix\radixinput1.txt 



## PROBLEM 3
This code implements the Stable Matching problem using the Gale Shapley algorithm. It starts with all men being free and keeps track of which women each man has already proposed to. Each woman maintains her current partner and a ranking of all men to quickly decide whether to accept a new proposal. The algorithm repeatedly lets a free man propose to the highest ranked woman on his preference list he hasn’t proposed to yet. If the woman is free, she accepts; if she already has a partner, she keeps the man she prefers more and rejects the other, making him free again. This process continues until no men are free. Finally, the function returns a dictionary mapping each man to the woman he is matched with.

DIRECTIONS: run the script while passing a test file and a answer file as a command-line argument
ex: python .\problem3.py .\testMatch\marriage_hundred.txt .\ansMatch\hundred_ans.txt 


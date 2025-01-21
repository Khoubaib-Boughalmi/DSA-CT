"""
    What is Insertion Sort?
    Insertion sort is a stable, in-place sorting algorithm. While it can be implemented recursively, the iterative approach is more common and efficient.

    How does it work?
    The algorithm divides the array into two parts: a sorted portion (initially containing the first element) and an unsorted portion. It iteratively picks the next element from the unsorted portion and inserts it into its correct position in the sorted portion by comparing it with the preceding elements.

    Time and Space Complexity:

        Worst case: O(n2) time complexity (e.g., when the array is sorted in reverse order) and O(1) space complexity.
        Best case: O(n) time complexity (e.g., when the array is already sorted) and O(1) space complexity.
"""

from typing import List

def insertionSort_ineficiente(nums: List[int]) -> None:
    i = 1
    while i < len(nums):
        j = i - 1
        current_index = i
        while(j >= 0 and nums[current_index] < nums[j]):
            nums[current_index], nums[j] = nums[j], nums[current_index]
            current_index -= 1
            j -= 1
        i += 1

def insertionSort_eficiente(nums: List[int]) -> None:
    i = 1
    while i < len(nums):
        
        current_value = nums[i]
        j = i - 1
        while j >= 0 and current_value < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j+1] = current_value
        i += 1

def main():
    lst = [3,4,12,4,5,6,7,2,1,0,6,2,1,3,78,9]
    insertionSort_ineficiente(lst)
    print(lst)
    lst = [3,4,12,4,5,6,7,2,1,0,6,2,1,3,78,9]
    insertionSort_eficiente(lst)
    print(lst)

if __name__ == "__main__":
    main()
"""
    What is merge sort: it is a stable sorting algorithm that allow us to sort input recursively in a O(n*logn) time complexity and O(n) space complexity, it works by splitting the input array in halves untill we have arrays of size 1, these arrays of size 1 can be considerate sorted, then these sorted chunks can be merged into a sorted array (preferably in place for space complexity), we can say that the merge sort can be devided into 2 section a devide section and a concor section ==> spliting the table, then merge the chunks
"""

from typing import List

"""
    sort 2 sorted arrays into the original array: nums[left:mid+1] and nums[mid+1:right+1]
    starting position of original array: left
    end position of original array: right

    Note: we used +1 in `nums[left:mid+1] and nums[mid+1:right+1]` because the slicing is exclusive
    exp: lhs = [1,2,5,7] rhs = [5,2,4,3] ==> nums = [1,2,2,3,4,5,5,7]
"""
def merge(nums: List[int], left: int, mid: int, right: int):
    lhs = nums[left:mid+1]
    rhs = nums[mid+1:right+1]

    i, j = 0, 0
    start = left

    while i < len(lhs) and j < len(rhs):
        if lhs[i] <= rhs[j]:
            nums[start] = lhs[i]
            i += 1
        else:
            nums[start] = rhs[j]
            j += 1
        start += 1

    while i < len(lhs):
        nums[start] = lhs[i]
        start += 1
        i += 1
    while j < len(rhs):
        nums[start] = rhs[j]
        start += 1
        j += 1

    
def mergeSort(nums: List[int], left, right):
    
    if left >= right:
        return
    mid = left + (right - left) // 2

    mergeSort(nums, left, mid)
    mergeSort(nums, mid + 1, right)

    merge(nums, left, mid, right)

def main():
    lst = [4,2,1,5,3,6,3,4,5,7,0]
    mergeSort(lst, 0, len(lst) - 1)
    print(lst)

if __name__ == "__main__":
    main()
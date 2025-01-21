from typing import List

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
        
def mergeSort(nums: List[int], left: int, right: int):

    if left >= right:
        return
    mid = left + (right - left) // 2

    mergeSort(nums, left, mid)
    mergeSort(nums, mid + 1, right)

    merge(nums, left, mid, right)

def main():
    lst = [3,4,2,1,6,5]
    mergeSort(lst, 0, len(lst) - 1)
    print(lst)

if __name__ == "__main__":
    main()

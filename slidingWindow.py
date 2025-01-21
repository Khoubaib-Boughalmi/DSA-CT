from typing import List

def max_sum_window(lst: List[int], size: int) -> int:
    if size > len(lst):
        return -1

    left, right = 0, size
    currentSum = sum(lst[:size])
    currentMax = currentSum

    while right < len(lst):
        currentSum = currentSum - lst[left] + lst[right]
        currentMax = max(currentMax, currentSum)
        right += 1
        left += 1
    return currentMax

def sortColors(nums: list[int]):
    left, right = 0, len(nums) - 1
    last_zero_pos = 0
    last_tow_pos = len(nums) - 1
    i = 0
    while i < len(nums):
        if nums[left] == 0:
            nums[left], nums[last_zero_pos] = nums[last_zero_pos], nums[left]
            last_zero_pos += 1
            left += 1
        elif nums[left] == 2:
            nums[left], nums[last_tow_pos] = nums[last_tow_pos], nums[left]
            last_tow_pos -= 1
        i+=1
    print(nums)


def main():
    lst = [1,1,2,0,0,2,2,0,1,0,0,2]
    sortColors(lst)
if __name__ == "__main__":
    main()
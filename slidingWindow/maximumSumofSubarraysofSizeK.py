"""
    nums: [2, 1, 5, 1, 3, 2]
"""

from typing import List

def maximumSumofSubarraysofSizeK_bruteForce(nums: List[int], k:int) -> int:
    max_k_sum = 0
    for i in range(0, len(nums) - k + 1):
        current_sum = 0
        for j in range(i, i+k):
            current_sum += nums[j]
        max_k_sum = max(max_k_sum, current_sum)
    return max_k_sum

def maximumSumofSubarraysofSizeK_efficient(nums: List[int], k:int) -> int:
    if not nums or k <= 0 or k > len(nums):
            return 0

    start, max_k_sum = 0, float('-inf')
    current_sum = sum(nums[:k])

    for end in range(k, len(nums)):
        max_k_sum = max(max_k_sum, current_sum)
        current_sum -= nums[start]
        current_sum += nums[end]
        start += 1
    return max_k_sum






def main():
    nums = [2, 1, 5, 1, 3, 2]
    k = 3
    print(maximumSumofSubarraysofSizeK_bruteForce(nums, k))
    print(maximumSumofSubarraysofSizeK_efficient(nums, k))

if __name__ == "__main__":
    main()
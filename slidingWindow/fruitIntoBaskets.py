"""
When to use sliding window
    Consider using the sliding window pattern for questions that involve searching for a continuous subsequence in an array or string that satisfies a certain constraint.
    If you know the length of the subsequence you are looking for, use a fixed-length sliding window. Otherwise, use a variable-length sliding window.
"""
from typing import List, _T

def maximum_number_fruits_slow(fruits: List[int]) -> int:
    max_fruites_count = 0

    for i in range(len(fruits)):
        for j in range(i, len(fruits)):
            if len(set(fruits[i:j+1])) <= 2:
                max_fruites_count = max(max_fruites_count, j-i+1)
            else:
                break
    return max_fruites_count

def maximum_number_fruits_efficient(fruits: List[int]) -> int:
    start = 0
    max_fruites_count = 0
    fruites_type_dict = {}

    if fruits == []:
        return 0

    for end in range(len(fruits)):
        fruites_type_dict[fruits[end]] = 1 + fruites_type_dict.get(fruits[end], 0)
        while len(fruites_type_dict) > 2:
            fruites_type_dict[fruits[start]] -= 1
            if fruites_type_dict[fruits[start]] == 0:
                del fruites_type_dict[fruits[start]]
            start += 1
        max_fruites_count = max(max_fruites_count, sum(fruites_type_dict.values()))
    return max_fruites_count

# def dynamic_sliding_window_template(input: List[_T]):
#     state = # choose appropriate data structure
#     start = 0
#     max_ = 0

#     for end in range(len(nums)):
#         # extend window
#         # add nums[end] to state in O(1) in time

#         while state is not valid:
#             # repeatedly contract window until it is valid again
#             # remove nums[start] from state in O(1) in time
#             start += 1

#         # INVARIANT: state of current window is valid here.
#         max_ = max(max_, end - start + 1)

#     return max_


def main():
    fruits = [3, 3, 2, 1, 2, 1, 0]
    print(maximum_number_fruits_efficient(fruits))
    print(maximum_number_fruits_slow(fruits))

if __name__ == "__main__":
    main()
from random import random
import heapq


"""
    start from the end of the array up to start, if the newwly added value is smaller than its parrent bubbled it up
"""

def heapify(nums: list[int]) -> list[int]:
    heap = list(nums)
    for parent_index in range(len(heap) // 2 - 1, -1, -1):
        parent_tmp = parent_index
        while True:
            left_child_id = 2 * parent_tmp + 1
            right_child_id = 2 * parent_tmp + 2

            if left_child_id >= len(heap): # no child
                break

            min_child_index = left_child_id
            if right_child_id < len(heap) and heap[right_child_id] < heap[left_child_id]:
                min_child_index = right_child_id

            if heap[min_child_index] < heap[parent_tmp]:
                heap[min_child_index], heap[parent_tmp] = heap[parent_tmp], heap[min_child_index]
                parent_tmp = min_child_index
            else:
                break
    return heap

def push_node(heap: list[int], new_node) -> None:
    heap.append(new_node)
    index = len(heap) - 1
    parent_index = (index - 1) // 2
    print(parent_index)
    while(parent_index >= 0 and heap[index] < heap[parent_index]):
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        index = parent_index
        parent_index = (parent_index - 1) // 2

def rand_list_gen(size: int) -> list[int]:
    return [int(random() * 100) for _ in range(size)]

# def test_heapify() -> None:
#     for i in range(50):
#         nums = rand_list_gen(int(random() * 100))
#         nums_copy = list(nums)
#         heapq.heapify(nums_copy)
#         if nums_copy != heapify(nums):
#             raise Exception(f"Failed test [{i}]:", nums)
#     print("Success")

def main():
    nums = [3,4,2,5,6,7,3,1]
    heap = heapify(nums)
    print(heap)
    # print(nums)

    # test_heapify()
    heap = [nums[0]]
    for num in nums[1:]:
        push_node(heap, num)
    print(heap)



if __name__ == "__main__":
    main()
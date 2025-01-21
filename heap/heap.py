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

def main():
    nums = [3,4,2,5,6,7,3,1]
    heap = heapify(nums)
    print(heap)
    print(nums)
if __name__ == "__main__":
    main()
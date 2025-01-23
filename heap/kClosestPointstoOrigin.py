from heapq import heapify, heappop, heappush
from math import sqrt

def calculate_distance(coords: list[int]) -> float:
    return round(sqrt(coords[0] ** 2 + coords[1] ** 2), 4)

def kClosestPointstoOrigin(points: list[list[int]], k: int) -> list[list[int]]:
    if not points or len(points) == 0:
        return []
    points = [[calculate_distance(point), point] for point in points]
    print(points)
    heapify(points)    
    result = []
    for _ in range(k):
        min_dist = heappop(points)
        result.append(min_dist[1])
    return result

def distance_squared(coords):
        return coords[0] ** 2 + coords[1] ** 2

def kClosest_optimized(points: list[list[int]], k: int):
    if not points or len(points) == 0:
        return []
    heap = [[-distance_squared(point), point] for point in points[:k]]
    heapify(heap)
    for point in points[k:]:
        current_distance_squared = distance_squared(point)
        if current_distance_squared < -heap[0][0]:
            heappop(heap)
            heappush(heap, [-current_distance_squared, point])
            
    return [point for _, point in heap]

def main():
    points = [[3,4],[2,2],[1,1],[0,0],[5,5]]
    k = 3
    # solution = kClosestPointstoOrigin(points, k)
    # print(solution)
    solution = kClosest_optimized(points, k)
    print(solution)
main()

[[5.0, [3, 4]], [2.8284271247461903, [2, 2]], [25.019992006393608, [1, 25]], [0.0, [0, 0]], [7.0710678118654755, [5, 5]]]
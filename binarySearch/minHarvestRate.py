def minHarvestRate_bruteForce(apples: list[int], h: int) -> int:
    start = 1
    while True:
        current_harvest_time = 0
        for i in range(0, len(apples)):
            if apples[i] % start == 0:
                current_harvest_time += apples[i]//start
            else:
                current_harvest_time += apples[i]//start + 1
        if current_harvest_time <= h:
            return start
        start += 1

def calculate_harvest_rate(apples: list[int], rate: int) -> int:
    current_harvest_time = 0
    for apple in apples:
        current_harvest_time += (apple + rate - 1) // rate  # Round up division
    return current_harvest_time

def minHarvestRate_binarysearch(apples: list[int], h: int) -> int:
    rates = [i for i in range(0, max(apples)+1)]
    start, end = 1, len(rates) - 1
    while start != end:
        mid = ((end + start) // 2) + 1
        if calculate_harvest_rate(apples, mid) > h:
            start = mid + 1
        else:
            end = mid
    return start

    

def main():
    apples = [25, 9, 23, 8, 3]
    h = 5
    # print(minHarvestRate_bruteForce(apples, h))
    print(minHarvestRate_binarysearch(apples, h))

main()
import heapq


def find_kth_largest(nums, k):

    min_heap = []

    for num in nums:

        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


def main():

    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    print(find_kth_largest(nums, k))


if __name__ == "__main__":
    main()
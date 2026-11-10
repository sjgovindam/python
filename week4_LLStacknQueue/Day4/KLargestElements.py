import heapq


def find_k_largest(nums, k):

    min_heap = []

    for num in nums:

        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return sorted(min_heap, reverse=True)


def main():

    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    print(find_k_largest(nums, k))


if __name__ == "__main__":
    main()
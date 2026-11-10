import heapq
from collections import Counter


def top_k_frequent(nums, k):

    # Step 1: Count frequency
    freq = Counter(nums)

    # Step 2: Create Min Heap
    heap = []

    # Step 3: Insert elements
    for num, count in freq.items():

        heapq.heappush(heap, (count, num))

        # Keep only K elements
        if len(heap) > k:
            heapq.heappop(heap)

    # Step 4: Extract result
    result = []

    while heap:
        count, num = heapq.heappop(heap)
        result.append(num)

    return result


def main():

    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    result = top_k_frequent(nums, k)

    print("Top", k, "frequent elements:", result)


if __name__ == "__main__":
    main()

def top_k_frequent(nums, k):

    # Step 1: Count frequency using dictionary
    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    # Step 2: Create buckets
    # Index represents frequency
    bucket = [[] for _ in range(len(nums) + 1)]

    # Step 3: Place numbers into frequency buckets
    for num, count in frequency.items():
        bucket[count].append(num)

    # Step 4: Collect top k frequent elements
    result = []

    for pos in range(len(bucket) - 1, 0, -1):

        if bucket[pos]:
            result.extend(bucket[pos])

        if len(result) >= k:
            return result[:k]

    return result


# Main function
def main():

    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    result = top_k_frequent(nums, k)

    print(result)


if __name__ == "__main__":
    main()

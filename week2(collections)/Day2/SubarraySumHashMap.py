#Prefix sum
#https://www.youtube.com/watch?v=YxRmeRyVQm4
def count_subarrays(nums, k):

    prefix_map = {0: 1}

    prefix_sum = 0
    count = 0

    for num in nums:

        prefix_sum += num

        required_sum = prefix_sum - k

        if required_sum in prefix_map:
            count += prefix_map[required_sum]

        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count


def main():
    nums = [1, 2, 3]
    k = 3

    print(count_subarrays(nums, k))


if __name__ == "__main__":
    main()
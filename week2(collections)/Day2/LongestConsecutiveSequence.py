
def longest_consecutive(nums):

    # Step 1: Convert list into set
    num_set = set(nums)

    longest = 0

    # Step 2: Check consecutive sequences
    for num in num_set:

        # Start counting only if num is the beginning
        if num - 1 not in num_set:

            current_num = num
            current_length = 1

            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            longest = max(longest, current_length)

    return longest


def main():

    nums = [100, 4, 200, 1, 3, 2]

    result = longest_consecutive(nums)

    print("Longest consecutive length:", result)


if __name__ == "__main__":
    main()

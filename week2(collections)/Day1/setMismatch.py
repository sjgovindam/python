
def find_error_nums(nums):

    seen = set()

    duplicate = -1
    missing = -1

    # Find duplicate
    for num in nums:

        if num in seen:
            duplicate = num
        else:
            seen.add(num)

    # Find missing
    for i in range(1, len(nums) + 1):

        if i not in seen:
            missing = i
            break

    return [duplicate, missing]




nums = [1, 2, 2, 4]

result = find_error_nums(nums)

print(result)



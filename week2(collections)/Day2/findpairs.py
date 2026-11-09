def find_pairs(nums, target):

    seen = set()
    result = []

    for num in nums:

        complement = target - num

        if complement in seen:
            result.append((complement, num))

        seen.add(num)

    return result


def main():
    nums = [2, 7, 11, 15, 3, 6]
    target = 9

    print(find_pairs(nums, target))


if __name__ == "__main__":
    main()
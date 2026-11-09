
def two_sum(nums, target):

    hashmap = {}

    for i in range(len(nums)):

        complement = target - nums[i]

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[nums[i]] = i

    return []


def main():

    nums = [2, 7, 11, 15]
    target = 9

    result = two_sum(nums, target)

    print(result)


if __name__ == "__main__":
    main()

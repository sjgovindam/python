def rotate(nums, k):

    k = k % len(nums)

    nums.reverse()

    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    nums = [1, 2, 3, 4, 5, 6, 7]
nums = [1, 2, 3, 4, 5, 6, 7]
k = 2
rotate(nums, k)
print(nums)
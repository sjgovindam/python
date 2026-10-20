def rotate_left(nums, k):

    k = k % len(nums)

    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    nums.reverse()



nums = [1, 2, 3, 4, 5, 6, 7]
k = 2
rotate_left(nums, k)
print(nums)

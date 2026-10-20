def maxsubarray(nums):
    currentsum=nums[0]
    maxsum=nums[0]

    for i in range(1, len(nums)):
        currentsum=max(nums[i],currentsum+nums[i])
        maxsum=max(currentsum,maxsum)
    return maxsum
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxsubarray(nums))
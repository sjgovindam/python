def minsubarraysum(nums):
    currentsum=nums[0]
    minsum=nums[0]

    for i in range(1,len(nums)):
        currentsum=min(nums[i],currentsum+nums[i])
        minsum=min(currentsum,minsum)
    return minsum

nums = [3, -4, 2, -3, -1, 7, -5]
print(minsubarraysum(nums))

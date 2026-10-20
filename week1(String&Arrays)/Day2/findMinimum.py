def findmin(nums):
    min=nums[0]
    for i in nums:
        if i<min:
            min=i
    return min
nums=[22,3,4,77,99]
print(findmin(nums))
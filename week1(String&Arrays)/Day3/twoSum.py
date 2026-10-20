def twosum(nums,target):

    seen={}

    for i in range(len(nums)):
        complement= target-nums[i]

        if complement in seen:
            return [seen[complement],i]
        seen[nums[i]]=i
    return[-1,-1]

nums=[22,34,56,74,12,4,15,1]
target=19
result=twosum(nums,target)
print(result)
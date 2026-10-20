def movezeroes(nums):
    index=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[index]=nums[i]
            index+=1
    while index < len(nums):
        nums[index]=0
        index+=1
nums=[1,0,20,30,0,45,3427,89,0]
movezeroes(nums)
print(nums)

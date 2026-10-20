def majorityelements(nums):
    count=0
    candidate=0

    for num in nums:

        if count ==0:
            candidate=num
        if candidate==num:
            count+=1
        else:
            count-=1
    return candidate
nums=[2,2,2,1,1,1,2,2]
print(majorityelements(nums))
            
def missingNo(nums,n):
    expectedsum=n*(n+1)/2
    originalsum=0
    for i in nums:
        originalsum+=i
    
    return expectedsum-originalsum

nums=[1,2,3,5,6]
n=6
print(missingNo(nums,n))
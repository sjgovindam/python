def largestElement(num):
    #num=[1,2,4,10,7,8,0]
    largest=num[0]
    for i in range(1,len(num)):
        if num[i]>largest:
            largest=num[i]
    return largest

print(largestElement(num=[1,2,4,12,7,8,0]))

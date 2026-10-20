def secondLargestElement(num):
    largest=float('-inf')
    secondLargest=float('-inf')

    for i in num:
        if i>largest:
            largest=i
            secondLargest=largest
        elif i>secondLargest and i != largest:
            secondLargest=i
    return secondLargest
num=[1,3,25,7,10,15]
print(secondLargestElement(num))

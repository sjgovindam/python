def removeduplicates(num):
    unique=set()
    for i in num:
        unique.add(i)
    return unique

num=[1,2,3,4,5,5,6,7,8,9,9]
print(removeduplicates(num))
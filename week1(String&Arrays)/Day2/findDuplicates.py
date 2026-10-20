def findDuplicate(num):
    seen =set()
    duplicates = set()

    for i in num:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
    return duplicates
num =[1,2,3,3,2,1,2,4,4,5,6,7,8,9]
print(findDuplicate(num))

def intersection(arr1,arr2):
    seen=set(arr1)
    result=set()

    for num in arr2:
        if num in seen:
            result.add(num)
    return list(result)
arr1=[1,2,3,4,5,6]
arr2=[1,3,7,8,9]
result=intersection(arr1,arr2)
print(result)
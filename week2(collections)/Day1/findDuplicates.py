def find_duplicates(arr):

    seen = set()
    duplicates = set()

    for num in arr:

        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return duplicates
arr = [1, 2, 3, 4, 2, 5, 3, 6, 1]

print("Duplicates:", find_duplicates(arr))
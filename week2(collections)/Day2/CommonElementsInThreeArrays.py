
def common_elements(arr1, arr2, arr3):

    result = []

    i = 0
    j = 0
    k = 0

    while i < len(arr1) and j < len(arr2) and k < len(arr3):

        # All three elements are equal
        if arr1[i] == arr2[j] == arr3[k]:

            # Avoid duplicates
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])

            i += 1
            j += 1
            k += 1

        # Move pointer of the smallest element
        elif arr1[i] < arr2[j]:
            i += 1

        elif arr2[j] < arr3[k]:
            j += 1

        else:
            k += 1

    return result


def main():

    arr1 = [1, 5, 10, 20, 40, 80]
    arr2 = [6, 7, 20, 80, 100]
    arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

    result = common_elements(arr1, arr2, arr3)

    print(result)


if __name__ == "__main__":
    main()

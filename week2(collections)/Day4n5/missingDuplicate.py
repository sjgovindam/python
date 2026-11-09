
def main():

    arr = [1, 2, 2, 4, 5]
    n = len(arr)

    seen = set()
    duplicate = -1

    expected_sum = n * (n + 1) // 2
    actual_sum = 0

    for num in arr:

        actual_sum += num

        if num in seen:
            duplicate = num
        else:
            seen.add(num)

    missing = expected_sum - (actual_sum - duplicate)

    print("Duplicate:", duplicate)
    print("Missing:", missing)


if __name__ == "__main__":
    main()

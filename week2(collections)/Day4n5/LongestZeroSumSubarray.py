
def main():

    arr = [15, -2, 2, -8, 1, 7, 10, 23]

    prefix_map = {}

    total = 0
    max_length = 0

    for i in range(len(arr)):

        total += arr[i]

        if total == 0:
            max_length = i + 1

        if total in prefix_map:

            length = i - prefix_map[total]
            max_length = max(max_length, length)

        else:
            prefix_map[total] = i

    print("Longest zero-sum subarray length:", max_length)


if __name__ == "__main__":
    main()

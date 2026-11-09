
def main():

    arr = [1, 5, 3, 4, 2]
    k = 2

    seen = set(arr)
    result = set()

    for num in arr:

        if num + k in seen:
            result.add((num, num + k))

        if num - k in seen:
            result.add((num - k, num))

    for pair in result:
        print(pair)


if __name__ == "__main__":
    main()

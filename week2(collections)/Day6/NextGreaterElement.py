
def next_greater(arr):

    n = len(arr)

    result = [-1] * n

    stack = []

    for i in range(n - 1, -1, -1):

        # Remove smaller or equal elements
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # Find next greater element
        if stack:
            result[i] = stack[-1]

        # Push current element
        stack.append(arr[i])

    return result


def main():

    arr = [4, 5, 2, 10, 8]

    print(next_greater(arr))


if __name__ == "__main__":
    main()

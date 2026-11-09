
def first_unique(s):

    frequency = {}

    # Step 1: Count frequency
    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    # Step 2: Find first unique character
    for ch in s:
        if frequency[ch] == 1:
            return ch

    return None


def main():

    s = "swiss"

    result = first_unique(s)

    if result is not None:
        print("First unique character:", result)
    else:
        print("No unique character found")


if __name__ == "__main__":
    main()

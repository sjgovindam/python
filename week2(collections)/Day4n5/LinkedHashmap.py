
def main():

    s = "programming"

    frequency = {}

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    for ch, count in frequency.items():
        print(ch, "=", count)


if __name__ == "__main__":
    main()

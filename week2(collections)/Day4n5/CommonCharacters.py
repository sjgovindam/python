
def main():

    str1 = "programming"
    str2 = "gaming"

    set2 = set(str2)

    common = []

    for ch in str1:
        if ch in set2 and ch not in common:
            common.append(ch)

    print(common)


if __name__ == "__main__":
    main()


def main():

    s = "Java Python Spring Java Python"

    words = s.split()

    seen = set()

    for word in words:

        if word in seen:
            print("First repeated word:", word)
            return

        seen.add(word)

    print("No repeated word found")


if __name__ == "__main__":
    main()

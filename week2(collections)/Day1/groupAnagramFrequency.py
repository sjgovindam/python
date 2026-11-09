
def group_anagrams(strs):

    if not strs:
        return []

    hashmap = {}

    for word in strs:

        # Create frequency array
        count = [0] * 26

        # Count character frequency
        for ch in word:
            count[ord(ch) - ord('a')] += 1

        # Convert frequency list into tuple key
        key = tuple(count)

        # Add word to its anagram group
        if key not in hashmap:
            hashmap[key] = []

        hashmap[key].append(word)

    return list(hashmap.values())


def main():

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    result = group_anagrams(strs)

    print(result)


if __name__ == "__main__":
    main()

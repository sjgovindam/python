
def find_unique(s):

    frequency = {}

    # Count character frequency
    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    # Find unique characters
    for ch in s:
        if frequency[ch] == 1:
            print(ch, end=" ")



s = "programming"

find_unique(s)

def is_anagram(s1, s2):

    if len(s1) != len(s2):
        return False

    frequency = {}

    for ch in s1:
        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in s2:
        if ch not in frequency or frequency[ch] == 0:
            return False

        frequency[ch] -= 1

    return True
s1 = "listen"
s2 = "silont"
print(is_anagram(s1, s2))
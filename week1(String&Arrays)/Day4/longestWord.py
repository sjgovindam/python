def find_longest_word(s):
    words=s.split()
    longest=""

    for word in words:
        if len(word)>len(longest):
            longest=word
    return longest
s="I love Programming"
longest=find_longest_word(s)
print("Longest word:", longest)
print("Length:", len(longest))
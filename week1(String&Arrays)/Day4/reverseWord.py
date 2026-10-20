def reverse_word(s):
    word=s.split()
    word.reverse()
    return " ".join(word)
s="I love Programming"
print(reverse_word(s))
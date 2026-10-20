def reverse_each_word(s):
    words=s.split()
    reverse_words=[]

    for word in words:
        reverse_words.append(word[::-1])
    return " ".join(reverse_words)
s="I love Programming"
print(reverse_each_word(s))
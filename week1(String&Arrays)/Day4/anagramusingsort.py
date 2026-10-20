def is_anagram(s1,s2):
    if len(s1)!=len(s2):
        return false
    return sorted(s1)==sorted(s2)

s1="lsiten"
s2="silont"
print(is_anagram(s1,s2))
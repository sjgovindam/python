def is_rotation(s1,s2):
    if len(s1) !=len(s2):
        return False

    combined=s1+s2

    return s2 in combined
s1 = "abcd"
s2 = "cdab"

print(is_rotation(s1, s2))
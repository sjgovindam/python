def compress(s):
    if not s:
        return ""

    result = []
    count = 1

    for i in range(len(s)):

        if i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
        else:
            result.append(s[i])
            result.append(str(count))
            count = 1

    return "".join(result)


s = "aaabbc"
print(compress(s))
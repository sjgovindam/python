def longestCommonprefix(str):
    if not str:
        return ""

    result=[]

    str.sort()
    first=str[0]
    last=str[len(str)-1]

    for i in range(min(len(first), len(last))):
        if first[i]!=last[i]:
            break
        result.append(first[i])
    return "".join(result)
strs = ["flower", "flow", "flight"]
print(longestCommonprefix(strs))

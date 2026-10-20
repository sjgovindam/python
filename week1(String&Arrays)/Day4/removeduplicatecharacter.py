def removeduplicate_char(s):
    seen=set()
    result=[]

    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return "".join(result)
s="Programming"
print(removeduplicate_char(s))
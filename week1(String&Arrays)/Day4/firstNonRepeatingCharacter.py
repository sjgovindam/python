def first_non_repeating_char(s):
    frequency={}
    for ch in s:
        frequency[ch]=frequency.get(ch,0)+1
    for ch in s:
        if frequency[ch]==1:
            return ch
    return None
s="programming"
result=first_non_repeating_char(s)
if result is not None:
    print(result)
else:
    print("No non-repeating character")
def count_frequency(s):
    frequency={}
    for ch in s:
        frequency[ch]=frequency.get(ch,0)+1
    return frequency

s="hello"
result=count_frequency(s)
for ch, count in result.items():
    print(ch, "=", count)

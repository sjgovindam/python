def count_frequency(s):
    frequency={}

    for ch in s:
        frequency[ch]=frequency.get(ch,0)+1
    print(frequency)

s="hello"
count_frequency(s)
def non_repeating_char(s):
    frequency={}

    for ch in s:
        frequency[ch]=frequency.get(ch,0)+1
    for ch in frequency:
        if frequency[ch]==1:
            print(ch,end="")

s="programming"
non_repeating_char(s)


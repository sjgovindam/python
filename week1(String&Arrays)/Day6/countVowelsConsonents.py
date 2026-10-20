def vowelsconson(str):
    vowels=0
    consonents=0
    str=str.lower()
    for ch in str:
        if ch in "aeiou":
            vowels+=1
        else:
            consonents+=1
    print("vowles:",vowels)
    print("consonents:",consonents)
str="Hello World"
vowelsconson(str)
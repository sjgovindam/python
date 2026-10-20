def reverseno(num):
    reverse=0
    while num !=0:
        digit=num%10
        reverse=reverse*10+digit
        num=num//10
    return reverse
num=123456
print(reverseno(num))
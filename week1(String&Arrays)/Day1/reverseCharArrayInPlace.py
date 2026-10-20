class ReverseCharArrayInPlace:

    def reverse(s):

        j = len(s) - 1

        for i in range(len(s) // 2):

            temp = s[i]
            s[i] = s[j]
            s[j] = temp

            j -= 1

    def main():

        s = ['h', 'e', 'l', 'l', 'o']

        ReverseCharArrayInPlace.reverse(s)

        print(s)


ReverseCharArrayInPlace.main()

def is_valid(s):

    stack = []

    for ch in s:

        if ch == '(':
            stack.append(')')

        elif ch == '{':
            stack.append('}')

        elif ch == '[':
            stack.append(']')

        elif not stack or stack.pop() != ch:
            return False

    return len(stack) == 0


def main():

    print(is_valid("()"))       # True
    print(is_valid("()[]{}"))   # True
    print(is_valid("(]"))       # False
    print(is_valid("([)]"))     # False
    print(is_valid("{[]}"))     # True


if __name__ == "__main__":
    main()

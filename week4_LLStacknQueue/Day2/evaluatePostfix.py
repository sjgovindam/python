def evaluate_postfix(tokens):

    stack = []

    for token in tokens:

        if token in ["+", "-", "*", "/"]:

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b

            elif token == "-":
                result = a - b

            elif token == "*":
                result = a * b

            elif token == "/":
                # Truncate division toward zero
                result = abs(a) // abs(b)
                if (a < 0) != (b < 0):
                    result = -result

            stack.append(result)

        else:
            stack.append(int(token))

    return stack.pop()


def main():

    tokens = ["2", "3", "4", "*", "+"]

    result = evaluate_postfix(tokens)

    print("Result:", result)


if __name__ == "__main__":
    main()
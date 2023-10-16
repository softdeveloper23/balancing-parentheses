# Function to balance parentheses in a string
def getMin(s):
    stack = []
    insertions = 0
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                insertions += 1
    insertions += len(stack)
    return insertions


# Test the function
def main():
    test_string = "(()))("
    print(
        f"The minimum number of insertions to balance the string '{test_string}' is {getMin(test_string)}."
    )


if __name__ == "__main__":
    main()

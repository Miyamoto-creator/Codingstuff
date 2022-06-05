# Python3 program to
# Print all combinations
# of balanced parentheses

# Wrapper over _printParenthesis()


def printParenthesis(str, n):
    if (n > 0):
        _printParenthesis(str, 0,
                          n, 0, 0)
    return "".join(str)


def _printParenthesis(str, pos, n,
                      open, close):
    if (close == n):
        for i in str:
            i
        return
    else:
        if (open > close):
            str[pos] = ')'
            _printParenthesis(str, pos + 1, n,
                              open, close + 1)
        if (open < n):
            str[pos] = '('
            _printParenthesis(str, pos + 1, n,
                              open + 1, close)


# Driver Code
n = 3
str = [""] * 2 * n
print("1: ",printParenthesis(str, n))

# This Code is contributed
# by mits.
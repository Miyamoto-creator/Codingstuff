def fibonacci(n: int) -> int:
    """Given a positive argument n, returns the nth term of the Fibonacci Sequence.
    """
    x, y = 0, 1
    for i in range(n):
        x, y = y, y + x
    return x
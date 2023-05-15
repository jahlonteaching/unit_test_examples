def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError(f"can't calculate factorial of negative number: {n}")

    return n * factorial(n-1)


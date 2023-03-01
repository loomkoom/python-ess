def example(n):
    if (n <= 0):
        return
    example(n - 3)
    print(n)
    example(n - 2)
    print(n)


print(example(6))

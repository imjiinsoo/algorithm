def ast(n):
    if n > 1:
        ast(n/2)
        ast(n/2)
    print("*", end='')

ast(5)

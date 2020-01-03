def func1(a, b):
    if b == 0:
        return a
    else:
        return func1(a, b-1) + 1

def multiply(a, b):
    if b == 0:
        return 0
    else:
        return func1(a, multiply(a, b-1))

print(multiply(7, 6))

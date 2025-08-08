# n!
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# nPr
def permutation(n, r):
    if r > n or n < 0 or r < 0:
        raise ValueError("Invalid values for n and r")
    return factorial(n) // factorial(n - r)

# nCr
def combination(n, r):
    if r > n or n < 0 or r < 0:
        raise ValueError("Invalid values for n and r")
    return factorial(n) // (factorial(r) * factorial(n - r))

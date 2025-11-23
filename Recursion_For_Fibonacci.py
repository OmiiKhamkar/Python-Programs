def fib(n):
    if n <= 1:   # base case
        return n
    return fib(n-1) + fib(n-2)

print(fib(6))   # Output: 8

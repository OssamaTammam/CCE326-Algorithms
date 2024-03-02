def fibonacci_top_down(n, memo={}):
    # if solved before just return the answer
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_top_down(n - 1) + fibonacci_top_down(n - 2)

    return memo[n]


def fibonacci_bottom_up(n):
    if n == 0 or n == 1:
        return n

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


n = 10
print(
    f"Top down approach = {fibonacci_top_down(n)}\nBottom up approach = {fibonacci_bottom_up(n)}"
)

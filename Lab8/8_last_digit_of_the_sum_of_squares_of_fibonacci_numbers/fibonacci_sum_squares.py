# Uses python3
from sys import stdin


def fibonacci_sum_squares_fast(n):

    fib = []
    fib.append(0)
    fib.append(1)
    sum = 0
    for i in range(2, 60):
        fib.append(fib[-1] + fib[-2])

    n = n % 60

    for j in range(n+1):
        sum += fib[j % 60]*fib[j % 60]

    return sum % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_fast(n))

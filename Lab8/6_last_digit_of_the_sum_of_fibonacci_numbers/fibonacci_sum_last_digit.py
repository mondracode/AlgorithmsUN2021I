# Uses python3
import sys


def fibonacci_sum_fast(n):
    n = n % 60
    if (n <= 1):
        return n

    fib = []
    fib.append(0)
    fib.append(1)
    sum = 1
    for i in range(2, n+1):
        fib.append(fib[-1] + fib[-2])
        sum += fib[-1]
        del fib[0:-2]
    return sum % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_fast(n))

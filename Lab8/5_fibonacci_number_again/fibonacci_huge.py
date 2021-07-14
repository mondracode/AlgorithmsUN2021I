# Uses python3
import sys


def get_pisano_period(m):
    previous = 0
    current = 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        if (previous == 0 and current == 1):
            return i + 1


def get_fibonacci_huge_fast(n, m):
    n = n % get_pisano_period(m)
    if (n <= 1):
        return n

    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(2, n+1):
        fib.append(fib[-1] + fib[-2])
        del fib[0:-2]
    return fib[-1] % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_fast(n, m))

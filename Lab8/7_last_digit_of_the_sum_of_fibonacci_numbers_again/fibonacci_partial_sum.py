# Uses python3
import sys


def fibonacci_partial_sum_fast(from_, to):
    if(to < from_):
        return -1

    fib = []
    fib.append(0)
    fib.append(1)
    sum = 0
    for i in range(2, 60):
        fib.append(fib[-1] + fib[-2])

    from_ = from_ % 60
    to = to % 60

    if(to < from_):
        to += 60

    for j in range(from_, to+1):
        sum += fib[j % 60]

    return sum % 10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_fast(from_, to))

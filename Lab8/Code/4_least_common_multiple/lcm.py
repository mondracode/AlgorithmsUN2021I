# Uses python3
import sys
import math


def gcd_fast(a, n):
    quo = math.floor(a/n)
    rem = a - (quo * n)

    if(rem == 0):
        return n
    else:
        return gcd_fast(n, rem)


def lcm_fast(a, b):
    return (a * b)//gcd_fast(a, b)


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_fast(a, b))

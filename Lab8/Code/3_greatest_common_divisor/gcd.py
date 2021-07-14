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


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_fast(a, b))

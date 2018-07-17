# Given 0<n,m<10^100 find  fib_n mod m.
# Sample Input 1:
#
# 1 10
# Sample Output 1:
#
# 1
# Sample Input 2:
#
# 7 10
# Sample Output 2:
#
# 3

n, m = [int(x) for x in input().split()]


def fib(n, m):
    if n == 0:
        return 0, 1
    else:
        a, b = fib(n // 2, m)
        c = a * (2 * b - a) % m
        d = (a ** 2 + b ** 2) % m

        if n % 2 == 0:
            return c, d
        else:
            return d, (c + d) % m


print(fib(n, m)[0])

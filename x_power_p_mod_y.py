# Given x, y, p: 0<x,y,p<10^100 compute x^p mod y

# Sample Input 1:
#
# 2 5 3
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# 2 100 10
# Sample Output 2:
#
# 24
x, y, p = [int(a) for a in input().split()]

import math


def findRemainderOfPower(a, p, n):
    return recurs_remainder(a, p, n)


def recurs_remainder(a, p, n):
    if p == 0:
        return 1
    if p == 1:
        return a % n
    else:
        rec = recurs_remainder(a, int(p // 2), n)
        if int(p // 2) == p - int(p // 2):
            return (rec * rec) % n
        else:
            return (rec * rec * (a % n)) % n


print(findRemainderOfPower(x, p, y))

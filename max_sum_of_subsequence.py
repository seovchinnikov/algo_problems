# Given 0<n<10^5 and sequence of a_i of length n.
# Need to compute max sum of subseq. a_i+a_i+1+…+a_j−1=S,i≤j.
# Sample Input 1:
#
# 2
# 1 1
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# 2
# 1 -1
# Sample Output 2:
#
# 1
n = int(input())
a = [int(x) for x in input().split()]


def calc_max_sum(a, st, end):
    if st > end:
        return 0

    m = int((st + end) / 2)
    max_sum_l = -99999999999
    sum_res = 0
    l = m - 1
    while l >= st:
        sum_res += a[l]
        if sum_res > max_sum_l:
            max_sum_l = sum_res
        l -= 1

    max_sum_r = -99999999999
    sum_res = 0
    r = m + 1
    while r <= end:
        sum_res += a[r]
        if sum_res > max_sum_r:
            max_sum_r = sum_res
        r += 1

    cur = a[m]
    if max_sum_l > 0:
        cur += max_sum_l

    if max_sum_r > 0:
        cur += max_sum_r

    return max([cur, calc_max_sum(a, st, m - 1),
                calc_max_sum(a, m + 1, end)])


print(calc_max_sum(a, 0, len(a) - 1))

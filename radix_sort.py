# radix sort
# Sample Input:
#
# 10 1
# 2 7 9 6 8 4 5 1 3 0
# Sample Output:
#
# 0 1 2 3 4 5 6 7 8 9
def count_sort_pos(a, m, pos):
    b = [0] * m
    for x in a:
        cur_pos = int(x / 10 ** pos) % 10
        b[cur_pos] += 1
    for i in range(1, m):
        b[i] += b[i - 1]
    r = [0] * len(a)
    for x in reversed(a):
        cur_pos = int(x / 10 ** pos) % 10
        r[b[cur_pos] - 1] = x
        b[cur_pos] -= 1
    return r


def rad_sort(a, k):
    for i in range(k):
        a = count_sort_pos(a, 10, i)

    return a


n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
result = list(a)
result = rad_sort(a, k)

for x in result:
    print(x, end=" ")

    # print(count_sort([1,99,22,55,22], 100))

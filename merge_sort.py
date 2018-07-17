# Sample Input 1:
# 3
# 1 2 3
# Sample Output 1:
# 1 2 3
# Sample Input 2:
# 3
# 3 1 2
# Sample Output 2:
# 1 2 3

n = int(input())
a = [int(x) for x in input().split()]


def merge_sort(a, start, end):
    if end - start <= 1:
        return
    mid = (end + start) // 2
    merge_sort(a, start, mid)
    merge_sort(a, mid, end)
    merge(a, start, mid, end)


def merge(a, start, mid, end):
    result = a[start:end]
    l = start
    r = mid
    cnt = 0
    while cnt < end - start:
        if a[l] < a[r]:
            result[cnt] = a[l]
            l += 1
        else:
            result[cnt] = a[r]
            r += 1
        cnt += 1
        if l == mid:
            result[cnt:end - start] = a[r:end]
            break
        if r == end:
            result[cnt:end - start] = a[l:mid]
            break

    a[start:end] = result[:]


merge_sort(a, 0, len(a))
for i in a:
    print(i, end=" ")

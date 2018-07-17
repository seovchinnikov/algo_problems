# Given array of n elements print the element that occurs > n//2 times or No if there is no such element
# Sample Input 1:
#
# 4
# 3 3 1 3
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# 3
# 1 2 3
# Sample Output 2:
#
# No
n = int(input())
ab = input().split()


def get_freq(a, elem):
    cnt = 0
    for elem_a in a:
        if elem_a == elem:
            cnt += 1
    return cnt


def find_major(a):
    l = len(a)

    if l == 1:
        return a[0]

    mid = int(l / 2.)
    el1 = find_major(a[:mid])
    el2 = find_major(a[mid:])

    if el1 == el2:
        return el1

    lcount = get_freq(a, el1)
    rcount = get_freq(a, el2)
    if lcount >= mid + 1:
        return el1
    elif rcount >= mid + 1:
        return el2
    else:
        return 'No'


print(find_major(ab))

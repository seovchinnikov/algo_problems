# given the the pattern and string print if the pattern occurred at the end of the string
# Sample Input 1:
#
# z
# abc
# Sample Output 1:
#
# No
# No
# No
# Sample Input 2:
#
# ab
# abbbab
# Sample Output 2:
#
# No
# Yes
# No
# No
# No
# Yes
P = input()
S = input()


def prefix(pattern):
    P = list(pattern)
    m = len(pattern)
    a = [0] * m
    k = 0

    for q in range(2, m + 1):
        while k > 0 and P[k] != P[q - 1]:
            k = a[k - 1]
        if P[k] == P[q - 1]:
            k += 1
        a[q - 1] = k

    return a


pref = prefix(P)


def subs(s, x):
    k, lenp, cnt = s
    cnt = 0
    while P[k] != x and k > 0:
        k = pref[k]
        k -= 1
        cnt += 1

    if P[k] == x:
        return [k == lenp - 1, [pref[k] if (k + 1) % lenp == 0  else  (k + 1) % lenp, lenp, cnt + 1]]
    else:
        return [False, [0, lenp, cnt + 1]]


startstate = [0, len(P), 0]
s = startstate
for x in S:
    ans, s = subs(s, x)
    print("Yes" if ans else "No")

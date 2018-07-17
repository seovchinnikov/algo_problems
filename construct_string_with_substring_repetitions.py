# find out the length of minimal substring of the full string repetitions of which can construct the full string
# Sample Input 1:
#
# ab
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# aaa
# Sample Output 2:
#
# 1
def zfun(s):
    n = len(s)
    z = [0] * n

    l, r = 0, 0
    z[0] = n
    for i in range(1, n):
        if i < r:
            k = i - l
            if z[k] < r - i:
                z[i] = z[k]
                continue
            l = i
        else:
            l = r = i
        while r < n and s[r - l] == s[r]:
            r += 1
        z[i] = r - l
    return z


S = input()

maxx = max(zfun(S)[1:])
r = len(S) % (len(S) - maxx)
if r == 0:
    print(len(S) - maxx)
else:
    print(len(S))

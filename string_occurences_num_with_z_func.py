# compute the number of occurrences of substring inside the string using z-function
# Sample Input 1:
#
# abc z
# Sample Output 1:
#
# 0
# Sample Input 2:
#
# abbbab ab
# Sample Output 2:
#
# 2
# Sample Input 3:
#
# abababa aba
# Sample Output 3:
#
# 3
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


S, P = input().split()

l = P + '#' + S

zf = zfun(l)
pl = len(P)
cnt = 0
for i in range(len(P) + 1, len(l)):
    if zf[i] == pl:
        cnt += 1

print(cnt)

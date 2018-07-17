# given pattern that consists of letters, ? and * print if string matches pattern
# Sample Input 1:
#
# ab
# ab
# Sample Output 1:
#
# Yes
# Sample Input 2:
#
# ?
# x
# Sample Output 2:
#
# Yes
# Sample Input 3:
#
# *aba*
# helloabaworld
# Sample Output 3:
#
# Yes
def match(s, p):
    if len(p) == 0:
        return len(s) == 0
    n = len(s)
    m = len(p)
    cache = [[False] * (m + 1) for _ in range(n+1)]

    cache[0][0] = True

    for j in range(m):
        if p[j] == '*':
            cache[0][j + 1] = cache[0][j]

    for i in range(n):
        for j in range(m):
            if p[j] == '?' or s[i] == p[j]:
                cache[i + 1][j + 1] = cache[i][j]
            elif p[j] == '*':
                cache[i + 1][j + 1] = cache[i + 1][j] or cache[i][j + 1]
            else:
                cache[i + 1][j + 1] = False


    return cache[n][m]



pattern = input()
s = input()

if match(s, pattern):
    print('Yes')
else:
    print('No')

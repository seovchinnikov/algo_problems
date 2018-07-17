# given n vars and k equations of type x0=x1 or x0!=x1 print if there is
#  such values of x_i that these conditions are satisfied
# Sample Input 1:
#
# 2 1
# x0!=x1
# Sample Output 1:
#
# Yes
# Sample Input 2:
#
# 2 1
# x0=x1
# Sample Output 2:
#
# Yes

from collections import defaultdict

n, k = map(int, input().split())
eq = []
neq = []
g1 = [set() for _ in range(n)]
g2 = [set() for _ in range(n)]
for _ in range(k):
    s = input()
    if '!' in s:
        a, b = s.split('!=')
        a, b = int(a[1:]), int(b[1:])
        neq.append([a, b])
        g1[a].add(b)
        g1[b].add(a)
    else:
        a, b = s.split('=')
        a, b = int(a[1:]), int(b[1:])
        eq.append([a, b])
        g2[a].add(b)
        g2[b].add(a)


def dfs(g, mat, s, v):
    mat[s][v] = True
    for i in g[v]:
        if not mat[s][i]:
            dfs(g, mat, s, i)


def transitive_closure(graph, n):
    reach = defaultdict(lambda: defaultdict(bool))  # [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dfs(graph, reach, i, i)

    for idx in range(n):
        reach[idx][idx] = False

    for idx, cons in enumerate(graph):
        for con in cons:
            reach[idx][con] = True

    return reach


clos1 = transitive_closure(g1, n)
clos2 = transitive_closure(g2, n)
for idx in range(n):
    clos2[idx][idx] = True
for idx1, _ in enumerate(clos1):
    for idx2, _ in enumerate(clos2):
        if clos1[idx1][idx2] and clos2[idx1][idx2]:
            print('No')
            quit()

print('Yes')

# given the oriented graph make topological sort
# Sample Input 1:
#
# 4 3
# 0 2
# 1 3
# 2 0
# Sample Output 1:
#
# 1
# 3
# 0 2
# Sample Input 2:
#
# 4 4
# 0 1
# 1 2
# 2 0
# 1 3
# Sample Output 2:
#
# 0 2 1
# 3
from __future__ import print_function

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)


def step1():
    visited = [False] * n
    pre = [None] * n
    post = [None] * n
    clock = 0


    def dfs(u, clock):
        #global clock
        pre[u] = clock
        clock += 1
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                clock = dfs(v, clock)
        post[u] = clock
        clock += 1
        return clock

    for u in range(n):
        if not visited[u]:
            clock = dfs(u, clock)

    return post

adj2 = [[] for _ in range(n)]
for idx, val in enumerate(adj):
    for v in val:
        adj2[v].append(idx)

def dfs2(u, adj, vis, res):
    vis[u] = True
    res.append(u)
    for v in adj[u]:
        if not vis[v]:
            dfs2(v, adj, vis, res)

post = step1()
post_i  = [b[0] for b in sorted(enumerate(post),key=lambda i:-i[1])]
visited = [False] * n
for i in post_i:
    if visited[i]:
        continue
    result = []
    dfs2(i, adj2, visited, result)
    for el in result:
        print(el, end=' ')
    print()
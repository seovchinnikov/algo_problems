# given the DAG that can have negative edges find out the shortest path between u and v
# Sample Input 1:
#
# 2 1
# 0 1 -1
# 0 1
# Sample Output 1:
#
# -1.0
# Sample Input 2:
#
# 3 1
# 0 1 0
# 0 2
# Sample Output 2:
#
# inf
from __future__ import print_function

from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(float, input().split())
    u, v = map(int, [u, v])
    adj[u].append((v, w))

s, f = map(int, input().split())

GRAY, BLACK = 0, 1


def topological(graph):
    order, enter, state = deque(), set(range(len(graph))), {}

    def dfs(node):
        state[node] = GRAY
        for k, _ in graph[node]:
            sk = state.get(k, None)
            if sk == BLACK:
                continue
            enter.discard(k)
            dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while enter:
        dfs(enter.pop())
    return order


c = [float('inf')] * n
c[s] = 0
res = topological(adj)
for i in res:
    for ne, w in adj[i]:
        if c[ne] > c[i] + w:
            c[ne] = float(c[i] + w)

print(c[f])

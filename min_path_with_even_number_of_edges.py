# find the min path from u to v that consists of even number of edges
# Sample Input 1:
#
# 2 1
# 0 1 1
# 0 1
# Sample Output 1:
#
# inf
# Sample Input 2:
#
# 3 1
# 0 1 1
# 0 2
# Sample Output 2:
#
# inf
from collections import defaultdict
from heapq import *

n, m = map(int, input().split())
adj = [[] for _ in range(n)]

adj2 = [[] for _ in range(2 * n)]
for _ in range(m):
    raw = input().split()
    u, v = map(int, raw[:2])
    d = float(raw[2])
    adj[u].append((d, v))
    adj2[u].append((d, v + n))
    adj2[u + n].append((d, v))

s, f = map(int, input().split())


def dijkstra(g, s, f):
    q, seen = [(0, s, ())], set()
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == f: return cost

            for c, v2 in g[v1]:
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))

    return float("inf")


res = dijkstra(adj2, s, f)
print(res)

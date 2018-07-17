# given the undirected graph with n vertices and m edges find the minimal spanning tree using Prim's algo
# Sample Input 1:
#
# 2 1
# 0 1 1
# Sample Output 1:
#
# 1.0
# Sample Input 2:
#
# 3 3
# 0 1 3
# 0 2 2
# 1 2 1
# Sample Output 2:
#
# 3.0
from heapq import heappush, heappop

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    raw = input().split()
    u, v = map(int, raw[:2])
    d = float(raw[2])
    adj[u].append([v, d])
    adj[v].append([u, d])


def minimum_tree_cost(adj):
    explored = set()
    res = 0
    unexplored = [(0, 0)]
    while unexplored:
        cost, chosen = heappop(unexplored)
        if chosen not in explored:
            explored.add(chosen)
            res += cost
            for neighbour, cost in adj[chosen]:
                if neighbour not in explored:
                    heappush(unexplored, (cost, neighbour))
    return res


print(minimum_tree_cost(adj))

# given the DAG compute the topological sort of the graph
# Sample Input 1:
#
# 3 0
# Sample Output 1:
#
# 2 1 0
# Sample Input 2:
#
# 3 2
# 2 1
# 0 1
# Sample Output 2:
#
# 0 2 1
from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)

GRAY, BLACK = 0, 1


def topological(graph):
    order, enter, state = deque(), set(range(len(graph))), {}

    def dfs(node):
        state[node] = GRAY
        for k in graph[node]:
            sk = state.get(k, None)
            if sk == BLACK: continue
            enter.discard(k)
            dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while enter:
        dfs(enter.pop())
    return order


res = topological(adj)
for i in res:
    print(i, end=' ')

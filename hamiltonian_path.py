# find the hamiltonian path and print it or print 'No' if it does not exist
# Sample Input 1:
#
# 3 0
# Sample Output 1:
#
# No
# Sample Input 2:
#
# 3 2
# 2 1
# 0 1
# Sample Output 2:
#
# No
from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(float, input().split())
    u, v = map(int, [u, v])
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


mat = [[None for _ in range(n)] for _ in range(n)]
for el1, _ in enumerate(adj):
    for el2 in adj[el1]:
        mat[el1][el2] = 0
res = topological(adj)
prev = None
res_els = []
for el in res:
    if prev is not None:
        if mat[prev][el] is None:
            print('No')
            quit()

    res_els.append(el)
    prev = el

for res_i in res_els:
    print(res_i, end=' ')

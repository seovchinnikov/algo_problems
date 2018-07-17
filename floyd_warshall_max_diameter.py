# Find the max distance between any pair of vertices in the graph using the Floyd-Warshall algo
# Sample Input 1:
#
# 4 2
# 0 2 1
# 1 3 -0.5
# Sample Output 1:
#
# inf
# Sample Input 2:
#
# 4 4
# 0 1 -1
# 1 2 3
# 2 3 2
# 0 3 1
# Sample Output 2:
#
# 2.0
n, m = map(int, input().split())
edges = [[None for _ in range(n)] for _ in range(n)]
for _ in range(m):
    raw = input().split()
    u, v = map(int, raw[:2])
    d = float(raw[2])
    edges[u][v] = d
    edges[v][u] = d

dist = [[float('inf') for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if edges[i][j] is not None:
            dist[i][j] = edges[i][j]

for i in range(n):
    dist[i][i] = 0

# print(dist)
for k in range(n):
    for i in range(n):
        for j in range(n):
            # print(dist)

            if i != j and dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

maxv = float('-inf')
for k in range(n):
    for i in range(n):
        if dist[i][k] > maxv and i != k:
            maxv = dist[i][k]

print(maxv)

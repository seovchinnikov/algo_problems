# print the shortest path between u and v (at the last line) in graph of n vertices and m edges
# or No of there is no such path
# Sample Input 1:
#
# 4 3
# 0 1
# 1 2
# 2 3
# 0 3
# Sample Output 1:
#
# 3
# 0 1 2 3
# Sample Input 2:
#
# 4 2
# 0 2
# 1 3
# 0 1
# Sample Output 2:
#
# No
from collections import deque

n, m = map(int,
           input().split())  # то же, что и [int(x) for x in input().split()]. map применяет функцию int ко всем элементам input().split()
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
s, f = map(int, input().split())  # начальная и конечная вершина пути

a = deque()

a.append(s)
visited = set()
pathes = deque([[s]])
while a:
    path = pathes.popleft()
    cur = a.popleft()
    if cur == f:
        print(len(path) - 1)
        for el in path:
            print(el, end=' ')
        quit()
    visited.add(cur)
    for nei in adj[cur]:
        if nei not in visited:
            pathes.append(path + [nei])
            a.append(nei)

print('No')

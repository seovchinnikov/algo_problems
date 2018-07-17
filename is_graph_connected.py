# given undirected graph with n vertices and m edges print 'Yes' if it's connected or some pair of unconnected vertices
# Sample Input 1:
#
# 2 1
# 0 1
# Sample Output 1:
#
# Yes
# Sample Input 2:
#
# 3 1
# 0 1
# Sample Output 2:
#
# 0 2
n, m = [int(x) for x in input().split()]
adj = [[] for _ in range(n)]
for _ in range(m):
    i, j = [int(x) for x in input().split()]
    adj[i].append(j)
    adj[j].append(i)

res = [False for _ in range(n)]


def dfs(i, ways, table):
    table[i] = True
    for way in ways[i]:
        if not table[way]:
            dfs(way, ways, table)
    return table


res = dfs(0, adj, res)
for i in range(n):
    if not res[i]:
        print(str(0) + ' ' + str(i))
        quit()

print('Yes')

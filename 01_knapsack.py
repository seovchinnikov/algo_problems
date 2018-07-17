# given max capacity of knapsack and n objects' weights
# print max weights of objects in the knapsack if you can take only one or zero objects of each type
# Sample Input 1:
#
# 10 3
# 1 4 8
# Sample Output 1:
#
# 9
# Sample Input 2:
#
# 20 4
# 5 7 12 18
# Sample Output 2:
#
# 19
W, n = [int(x) for x in input().split()]
wi = [int(x) for x in input().split()]

m = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(W + 1):
        if wi[i - 1] > j:
            m[i][j] = m[i - 1][j]
        else:
            m[i][j] = max(m[i - 1][j], m[i - 1][j - wi[i - 1]] + wi[i - 1])

print(m[n][W])

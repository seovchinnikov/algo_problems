# Sample Input 1:
#
# 3 2
# 1 1 1
# Sample Output 1:
#
# 1 1 1
# Sample Input 2:
#
# 5 5
# 4 3 2 3 4
# Sample Output 2:
#
# 2 3 3 4 4
n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

C = [0] * m
for i in range(m):
    C[i] = 0
for i in range(n):
    C[a[i]] = C[a[i]] + 1

b = 0
for j in range(m):
    for i in range(C[j]):
        a[b] = j
        b = b + 1

for el in a:
    print(el, end=' ')

# given the n items list and capacity of the continuous knapsack print how much it can handle at max.
# Sample Input:
#
# 3 50
# 60 20
# 100 50
# 120 30
# Sample Output:
#
# 180.000
n, W = [int(x) for x in input().split()]
c = [None] * n
w = [None] * n
for i in range(n):
    c[i], w[i] = [int(x) for x in input().split()]

pers = [-ci / float(wi) for ci, wi in zip(c, w)]
poses_sort = sorted(range(len(pers)), key=lambda k: pers[k])
total_w, total_n, total_c, i = 0, 0, 0, 0
while total_w < W and total_n < n:

    pos = poses_sort[i]
    total_w += w[pos]
    if total_w > W:
        dif_c = (total_w - W) / float(w[pos])
        total_c += c[pos] - dif_c * c[pos]
        break
    total_n += 1
    total_c += c[pos]
    i += 1

print("%.3f" % total_c)

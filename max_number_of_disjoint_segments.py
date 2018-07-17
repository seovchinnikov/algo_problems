# given n segments find max k such that there are k non-overlapping segments
# Sample Input 1:
#
# 1
# 1 2
# Sample Output 1:
#
# 1
# Sample Input 2:
#
# 3
# 1 3
# 2 3
# 1 2
# Sample Output 2:
#
# 2
n = int(input())
pairs = [None] * n
for i in range(n):
    pairs[i] = [int(x) for x in input().split()]

ind_sorted = sorted(range(len(pairs)), key=lambda x: pairs[x][1])
sorted_ints = [pairs[i] for i in ind_sorted]
# print(sorted_ints)

answer = 0
idx = 0
cur = sorted_ints[0][0]
for i in range(n):
    if sorted_ints[i][0] >= cur:
        answer += 1
        cur = sorted_ints[i][1]
    i += 1

print(answer)

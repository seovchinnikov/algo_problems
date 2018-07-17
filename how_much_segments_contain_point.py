# Given n segments, m points (in the first row), then segments and points itself,
# print how much segments contain every point
# Sample Input 1:
#
# 2 3
# 0 5
# 7 10
# 1 6 11
# Sample Output 1:
#
# 1 0 0
# Sample Input 2:
#
# 1 3
# -10 10
# -100 100 0
# Sample Output 2:
#
# 0 0 1
n, m = [int(x) for x in input().split()]
intervals = [None] * n
for i in range(n):
    intervals[i] = [int(x) for x in input().split()]
points = [int(x) for x in input().split()]

counter = [0] * len(points)
seg_num = 0
dict = {}
int_l = [interv[0] for interv in intervals]
int_r = [interv[1] for interv in intervals]

all_points = [(x, 'l') for x in int_l]
all_points += [(x, 'p') for x in points]
all_points += [(x, 'r') for x in int_r]
for i in range(len(points)):
    if points[i] not in dict:
        dict[points[i]] = [i]
    else:
        dict[points[i]].append(i)

all_points.sort(key=lambda x: x[0])

for p in all_points:
    if p[1] == 'l':
        seg_num += 1
    elif p[1] == 'r':
        seg_num -= 1
    else:
        all_poses = dict[p[0]]
        for pos in all_poses:
            counter[pos] = seg_num

for x in counter:
    print(x, end=" ")

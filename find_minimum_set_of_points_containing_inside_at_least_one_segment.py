# given n segments find out the min number of points and points itself such as every point is contained inside at least one segment
# Sample Input 1:
#
# 3
# 1 3
# 2 5
# 3 6
# Sample Output 1:
#
# 1
# 3
# Sample Input 2:
#
# 4
# 4 7
# 1 3
# 2 5
# 5 6
# Sample Output 2:
#
# 2
# 3 6
n = int(input())
intervals = [None] * n
for i in range(n):
    intervals[i] = [int(x) for x in input().split()]

rooms = [None] * n
filed_ints = 0
ind_sorted = sorted(range(len(intervals)), key=lambda x: intervals[x][1])
sorted_ints = [intervals[i] for i in ind_sorted]
while (filed_ints < n):
    base = None
    for i, interv in enumerate(sorted_ints):
        if rooms[i] is None:
            base = i
            break

    val = sorted_ints[base][1]
    # print(val)
    for i, interv in enumerate(sorted_ints):
        if rooms[i] is None:
            if interv[0] <= val and interv[1] >= val:
                rooms[i] = val
                filed_ints += 1

print(len(set(rooms)))
for el in set(rooms):
    print(el, end=' ')

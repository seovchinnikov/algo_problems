# Given n find out the max number of elements that sum up to n
# Sample Input 1:
#
# 4
# Sample Output 1:
#
# 2
# 1 3
# Sample Input 2:
#
# 6
# Sample Output 2:
#
# 3
# 1 2 3
n = int(input())


def maxsum(k):
    i = 1
    while (True):
        if (k < i):
            return i - 1
        else:
            k -= i
        i += 1


res = maxsum(n)
print(res)
sum = 0
for i in range(1, res):
    print(i, end=' ')
    sum += i
print(n - sum, end=' ')

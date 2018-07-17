# given two string compute levenstein distance
# Sample Input 1:
#
# ab
# ab
# Sample Output 1:
#
# 0
# Sample Input 2:
#
# short
# ports
# Sample Output 2:
#
# 3
str1 = input()
str2 = input()


def levenstein(s1, s2, pos1, pos2):
    cache = [[0 for x in range(pos2 + 1)] for x in range(pos1 + 1)]

    for iter1 in range(pos1 + 1):
        for iter2 in range(pos2 + 1):
            if iter2 == 0:
                cache[iter1][iter2] = iter1
            elif iter1 == 0:
                cache[iter1][iter2] = iter2

            elif s1[iter1 - 1] == s2[iter2 - 1]:
                cache[iter1][iter2] = cache[iter1 - 1][iter2 - 1]

            else:
                cache[iter1][iter2] = 1 + min(cache[iter1 - 1][iter2 - 1], cache[iter1][iter2 - 1],
                                              cache[iter1 - 1][iter2])
    return cache[pos1][pos2]


print(levenstein(str1, str2, len(str1), len(str2)))
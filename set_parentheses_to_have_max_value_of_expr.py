# given *-+ expression print max value ot it if you set up parentheses
# Sample Input 1:
#
# 1+2+3
# Sample Output 1:
#
# 6
# Sample Input 2:
#
# 2+2*2
# Sample Output 2:
#
# 8
def eval(a, b, oper):
    a = float(a)
    b = float(b)
    if oper == '*':
        return a * b
    elif oper == '-':
        return a - b
    elif oper == '+':
        return a + b


def maxim(equation):
    l = (len(equation) + 1) // 2

    maxims = [[0] * l for _ in range(l)]

    for i in range(l):
        maxims[i][i] = equation[2 * i]

    for s in range(l - 1):
        for i in range(l - s - 1):
            maxVal = float('-inf')
            j = i + s + 1

            for k in range(i, j):
                a4 = eval(maxims[i][k], maxims[k + 1][j], equation[2 * k + 1])
                maxVal = max([maxVal, a4])

                maxims[i][j] = maxVal

    return maxims[0][l - 1]


print(int(maxim(input())))

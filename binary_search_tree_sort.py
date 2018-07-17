# Sample Input 1:
#
# 2
# 1 0
# Sample Output 1:
#
# 0 1
# Sample Input 2:
#
# 4
# 1 2 3 4
# Sample Output 2:
#
# 1 2 3 4
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __nonzero__(self):
        return True

    def __bool__(self):
        return True

    def add(self, n):
        if self.contains(n.key):
            return
        if self.key is None:
            self.key = n.key
            return

        if n.key > self.key:
            if self.right is not None:
                self.right.add(n)
            else:
                self.right = n
        elif n.key < self.key:
            if self.left is not None:
                self.left.add(n)
            else:
                self.left = n

    def contains(self, x):
        if self.key is None:
            return False
        if self.key == x:
            return True
        if self.key < x and self.right is not None:
            return self.right.contains(x)
        elif self.left is not None:
            return self.left.contains(x)
        else:
            return False

    def sort(self):
        ans = []
        left = []
        right = []
        if self.left is not None:
            left = self.left.sort()
        if self.right is not None:
            right = self.right.sort()
        ans = left + [self.key] + right
        return ans

    def depth(self):
        return max(self.left.depth() if self.left else 0, self.right.depth() if self.right else 0) + 1


n = int(input())
a = [int(x) for x in input().split()]
root = Node(a[0])
for key in a[1:]:
    root.add(Node(key))
ans = root.sort()
for i in ans:
    print(str(i), end=' ')
    # print(root.sort())
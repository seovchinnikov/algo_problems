# given n - the number of operations and operations "Insert", "ExtractMax" with arguments (over the binary heap)
# print the results of operations if any
# Sample Input:
#
# 6
# Insert 200
# Insert 10
# ExtractMax
# Insert 5
# Insert 500
# ExtractMax
# Sample Output:
#
# 200
# 500
class PriorityQueue:
    def __init__(self, n):
        self.heap = [0] * n
        self.maxsize = n
        self.size = 0

    def push(self, el):
        self.heap[self.size] = el
        self.size += 1
        self.arise(self.size - 1)

    def pop(self):
        heap = self.heap
        last_element = heap[self.size - 1]  # heap.pop()
        self.size -= 1
        if not heap:
            return last_element
        item = heap[0]
        heap[0] = last_element
        self.sink()
        return item

    def sink(self):
        heap = self.heap
        length = self.size
        if length == 1:
            return
        par = 0
        while 2 * par < length:
            child = 2 * par
            if child + 1 < length and heap[child + 1] > heap[child]:
                child += 1
            if heap[child] < heap[par]:
                return
            heap[child], heap[par] = heap[par], heap[child]
            par = child

    def arise(self, child_index):
        heap = self.heap
        child = child_index
        while child > 0:
            parent = child // 2
            if heap[parent] > heap[child]:
                return
            heap[child], heap[parent] = heap[parent], heap[child]
            child = parent


n = int(input())
pq = PriorityQueue(n)
for _ in range(n):
    query = input().split()
    if query[0] == "Insert":
        pq.push(int(query[1]))
    elif query[0] == "ExtractMax":
        print(pq.pop())

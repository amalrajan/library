import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


class MinHeap:
    def __init__(self):
        self.A = []

    def parent(self, i):
        return (i - 1) // 2

    def heapify_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < len(self.A) and self.A[left] < self.A[i]:
            smallest = left
        if right < len(self.A) and self.A[right] < self.A[smallest]:
            smallest = right

        if smallest != i:
            self.A[i], self.A[smallest] = self.A[smallest], self.A[i]
            self.heapify_down(smallest)

    def heapify_up(self, i):
        par = self.parent(i)
        if i and self.A[par] > self.A[i]:
            self.A[i], self.A[par] = self.A[par], self.A[i]
            self.heapify_up(par)

    def empty(self):
        return self.A == []

    def heap_push(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A) - 1)

    def heap_pop(self):
        if not self.A:
            return None

        self.A[0] = self.A[-1]
        self.A.pop()
        self.heapify_down(0)

    def top(self):
        if not self.A:
            return None

        return self.A[0]


pq = MinHeap()
pq.heap_push(3)
pq.heap_push(1)
pq.heap_push(5)
print(pq.top())

pq.heap_pop()
print(pq.top())

pq.heap_pop()
print(pq.top())

pq.heap_pop()
print(pq.top())

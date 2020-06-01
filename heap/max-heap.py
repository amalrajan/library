import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def heapify_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < len(self.heap) and self.heap[left] > self.heap[i]:
            largest = i
        elif right < len(self.heap) and self.heap[right] > self.heap[i]:
            largest = i

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify_down(largest)

    def heapify_up(self, i):
        par = self.parent(i)
        if i and self.heap[par] < self.heap[i]:
            self.heap[i], self.heap[par] = self.heap[par], self.heap[i]
            self.heapify_up(par)

    def empty(self):
        return self.heap == []

    def heap_push(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def heap_pop(self):
        if not self.heap:
            return 

        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)

    def top(self):
        if not self.heap:
            return
        
        return self.heap[0]


pq = MaxHeap()
pq.heap_push(2)
pq.heap_push(3)

print(pq.top())

pq.heap_push(5)
print(pq.top())

pq.heap_pop()
pq.heap_pop()
print(pq.top())
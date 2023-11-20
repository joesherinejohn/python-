import sys
import heapq


class PriorityQueue:
    def __init__(self, table_capacity):
        self.table_capacity = table_capacity
        self.heap = []
        self.count = 0

    def enqueue(self, value, priority):
        print(self.heap)
        if len(self.heap) < self.table_capacity:
            heapq.heappush(self.heap, (priority, self.count, value))
            self.count += 1
            self.heap = sorted(self.heap, key=lambda x: x[0])
            print(self.heap)
        elif priority > self.heap[0][0]:
            self.heap = sorted(self.heap, key=lambda x: x[0])
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, (priority, self.count, value))
            self.count += 1
            self.heap = sorted(self.heap, key=lambda x: x[0])
            print(self.heap)

    def dequeue(self):
        if self.heap:
            # self.heap.pop()
            highest_first_element = self.heap[-1][0]

            filtered_permutations = [tup for tup in self.heap if tup[0] != highest_first_element or tup[1] != min(
                t[1] for t in self.heap if t[0] == highest_first_element)]
            self.heap = filtered_permutations
        self.heap = sorted(self.heap, key=lambda x: x[0])
        print(self.heap)

capacity = int(input().strip())
priority_queue = PriorityQueue(capacity)

for line in sys.stdin:
    tokens = line.strip().split()
    if tokens[0] == "enqueue":
        value, priority = int(tokens[1]), int(tokens[2])
        priority_queue.enqueue(value, priority)

    elif tokens[0] == "dequeue":
        priority_queue.dequeue()

# python-
A program for Priority Queue Implementation:
Each element is a pair containing a value and an associated priority. Elements are processed in the queue according to their priority. The value and priority are both integers.

The priority queue should have enqueue and dequeue methods:

The enqueue method must insert a given element into the queue
The dequeue method must remove the element with the highest priority first. If elements have the same priority, they must be removed in the order in which they were inserted.
The queue must also have a certain capacity, which is the maximum number of elements allowed in the data structure.

If the queue is full and contains at least one element with a priority less than the priority of an element to be inserted, the enqueue method must insert the new element by replacing the existing element with the lowest priority in the queue. If the queue is full but doesn't contain elements with the lower priority, the enqueue method must do nothing. Similarly, the dequeue method must do nothing if the queue is empty.

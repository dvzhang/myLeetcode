'''
Min Heap Construction
Implement a MinHeap class that supports:
- Building a min heap from an input array of integers.
- Inserting integers in the heap.
- Removing the heap's minimum / root value.
- Peeking at the heap's minimum / root value.
- Sifting integers up and down the heap, which is to be used when iserting and removing values.
Note that the heap should be represented in the form of an array.
'''
# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.


class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
    # Time O(n) Space O(1)

    def buildHeap(self, array):
        parentIdx = (len(array)-2)//2
        for currentIdx in reversed(range(parentIdx + 1)):
            self.siftDown(currentIdx, len(array)-1, array)
        return array
    # Time O(logn) Space O(1)

    def siftDown(self, currentIdx, endIdx, heap):
        childOne = 2*currentIdx + 1
        while childOne <= endIdx:
            childTwo = 2*currentIdx + 2
            if childTwo <= endIdx and heap[childTwo] < heap[childOne]:
                indexToSwap = childTwo
            else:
                indexToSwap = childOne
            if heap[indexToSwap] < heap[currentIdx]:
                self.swap(indexToSwap, currentIdx, heap)
                currentIdx = indexToSwap
                childOne = 2*currentIdx + 1
            else:
                return
    # Time O(logn) Space O(1)

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx-1)//2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx-1) // 2
    # Time O(1) Space O(1)

    def peek(self):
        return self.heap[0]
    # Time O(1) Space O(1)

    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
        value = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return value
    # Time O(1) Space O(1)

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
    # Time O(1) Space O(1)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
heap = MinHeap(array)
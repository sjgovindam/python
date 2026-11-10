import heapq


class MedianFinder:

    def __init__(self):

        # Max Heap (negative values)
        self.max_heap = []

        # Min Heap
        self.min_heap = []

    def addNum(self, num):

        # Add to appropriate heap
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Balance heaps
        if len(self.max_heap) > len(self.min_heap) + 1:

            value = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value)

        elif len(self.min_heap) > len(self.max_heap):

            value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -value)

    def findMedian(self):

        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]

        return (-self.max_heap[0] + self.min_heap[0]) / 2.0


def main():

    mf = MedianFinder()

    numbers = [5, 15, 1, 3, 8, 7]

    for num in numbers:
        mf.addNum(num)
        print("Added:", num, "Median:", mf.findMedian())


if __name__ == "__main__":
    main()
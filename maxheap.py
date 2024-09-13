class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)  # Add the new element at the end
        self._heapify_up(len(self.heap) - 1)  # Restore the heap property

    def extract_max(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        max_value = self.heap[0]
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()  # Move the last element to the root
            self._heapify_down(0)  # Restore the heap property
        else:
            self.heap.pop()  # Remove the last element if it's the only element
        return max_value

    def delete_element(self, value):
        try:
            index = self.heap.index(value)
        except ValueError:
            raise ValueError("Element not found in heap")
        
        # Move the last element to the index of the element to delete
        if index < len(self.heap) - 1:
            self.heap[index] = self.heap.pop()  # Replace the element with the last one
            self._heapify_down(index)  # Restore heap property after replacement
            self._heapify_up(index)
        else:
            self.heap.pop()  # If it's the last element, just pop it

    def print_heap(self):
        print(self.heap)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] <= self.heap[parent]:
                break
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent

    def _heapify_down(self, index):
        size = len(self.heap)
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index

        if left_child < size and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < size and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)


if __name__ == "__main__":
    max_heap = MaxHeap()

    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(5)
    max_heap.insert(15)
    max_heap.insert(30)

    print("Heap elements:", end=" ")
    max_heap.print_heap()  # Expected: [30, 20, 15, 5, 10]

    print("Extracted max:", max_heap.extract_max())  # Expected: 30
    print("Heap after extraction:", end=" ")
    max_heap.print_heap()  # Expected: [20, 10, 15, 5]

    max_heap.delete_element(10)
    print("Heap after deletion of 10:", end=" ")
    max_heap.print_heap()  # Expected: [20, 5, 15]

from heapq import *


def down_adjust_1(num_list, index, border):
    tmp = num_list[index]
    parent = index
    child = 2 * parent + 1
    while child < border:
        if child + 1 < border and num_list[border + 1] > num_list[border]:
            border += 1
        if tmp > num_list[child]:
            break
        num_list[parent] = num_list[child]
        parent = child
        child = 2 * child + 1
    if index != parent:
        num_list[parent] = tmp


class PriorityQueue:
    def __init__(self, e_list=None):
        if e_list:
            self._elements = list(e_list)
        else:
            self._elements = e_list

    def build_heap_1(self):
        num_list = self._elements
        if num_list:
            for i in range((len(self._elements) - 1) // 2, -1, -1):
                down_adjust_1(num_list, i, len(num_list))

    def up_adjust_1(self, data, border):
        num_list, child, parent = self._elements, border, (border - 1) // 2
        while child > 0 and data > num_list[parent]:
            num_list[child] = num_list[parent]
            child = parent
            parent = parent // 2
        num_list[child] = data

    def en_queue_1(self, data):
        self._elements.append(data)
        self.up_adjust_1(data, len(self._elements) - 1)

    def de_queue_1(self):
        if not self._elements:
            raise Exception('queue is empty')
        return self._elements[0]

    def build_heap(self):
        end = len(self._elements)
        for i in range(end // 2, -1, -1):
            self.down_adjust(self._elements[i], i, end)

    def en_queue(self, data):
        self._elements.append(None)
        self.up_adjust(data, len(self._elements) - 1)

    def de_queue(self):
        if not self._elements:
            raise Exception('in Peek')
        data = self._elements.pop()
        self.down_adjust(data, 0, len(self._elements))

    def up_adjust(self, elements, border):
        num_list, child, parent = self._elements, border, (border - 1) // 2
        while child > 0 and elements > num_list[parent]:
            num_list[child] = num_list[parent]
            child = parent
            parent = parent // 2
        num_list[child] = elements

    def down_adjust(self, data, index, border):
        elements, child_index, parent_index = self._elements, 2 * index + 1, index

        while child_index < border:
            if child_index + 1 < border \
                    and elements[child_index + 1] > elements[child_index]:
                child_index += 1
            if data >= elements[child_index]:
                break
            elements[parent_index] = elements[child_index]
            parent_index = child_index
            child_index = 2 * child_index + 1
        elements[parent_index] = data

    @property
    def elements(self):
        return self._elements


class HeapPriQueue(object):
    def __init__(self, heap_list=None):
        if heap_list is None:
            heap_list = []
        self.heap = heap_list
        heapify(self.heap)

    def enqueue(self, val):
        heappush(self.heap, val)

    def dequeue(self):
        return heappop(self.heap)


if __name__ == "__main__":
    lst = [5, 6, 8, 1]
    heap = HeapPriQueue(lst)
    print(heap.dequeue())  # 1
    heap.enqueue(3)
    print(heap.heap)  # [3, 5, 8, 6]

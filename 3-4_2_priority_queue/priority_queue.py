class PriorityQueue:
    def __init__(self, e_list=None):
        if e_list is None:
            e_list = []
        self._elements = list(e_list)
        if e_list:
            self.build_heap()

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
        return self._elements[0]

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

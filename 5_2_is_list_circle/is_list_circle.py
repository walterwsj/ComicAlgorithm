class LinkNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self, head=None):
        self.head = head

    def node_append(self, data):
        node = LinkNode(data)
        if self.head is None:
            self.head = node
        else:
            while self.head.next is not None:
                self.head = self.head.next
        self.head.next = node

    def is_link_circle(self):
        p1 = self.head
        p2 = self.head
        while p1 and p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 is p2:
                return True
        return False

    def get_circle_len(self):
        p1 = self.head
        p2 = self.head
        step = 0
        while p1 and p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            step += 1
            if p1 is p2:
                return step
        return None

    def get_cross_node(self):
        p1 = self.head
        p2 = self.head
        while p1 and p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 is p2:
                p1 = self.head
                while p1 and p2:
                    p1 = p1.next
                    p2 = p2.next
                    if p1 is p2:
                        return p1.data
        return None


if __name__ == "__main__":
    t = LinkList()
    node1 = LinkNode(1)
    node2 = LinkNode(2)
    node3 = LinkNode(3)
    node4 = LinkNode(4)
    node5 = LinkNode(5)
    node6 = LinkNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node3
    t.head = node1

    print(t.get_cross_node())

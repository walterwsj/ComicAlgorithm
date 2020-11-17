# 使用两个栈 A B
# A 栈入栈操作完成之后 便将所有元素出栈到B
# 出队的时候 将B栈内容输出

class MyQueue:
    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def en_queue(self, element):
        self.stack_a.append(element)

    def de_queue(self):
        if len(self.stack_b) == 0:
            if len(self.stack_a) == 0:
                return None
            else:
                while len(self.stack_a):
                    self.stack_b.append(self.stack_a.pop())
                return self.stack_b.pop()

    def en_queue_1(self, element):
        self.stack_a.append(element)

    def de_queue_1(self):
        if len(self.stack_b) == 0:
            if len(self.stack_a) == 0:
                return None
            else:
                while len(self.stack_a):
                    self.stack_b.append(self.stack_a.pop())
        return self.stack_b.pop()

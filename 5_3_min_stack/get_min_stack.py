class MinStack:
    def __init__(self):
        self.stack_main = []
        self.stack_slave = []

    def en_stack(self, num):
        self.stack_main.append(num)
        if len(self.stack_slave) == 0 or self.stack_slave[len(self.stack_slave)-1] > num:
            self.stack_slave.append(num)

    def de_stack(self):
        if len(self.stack_main) == 0:
            return None
        if self.stack_main[len(self.stack_main) - 1] == self.stack_slave[len(self.stack_slave)-1]:
            self.stack_main.pop()
            return self.stack_slave.pop()
        else:
            return self.stack_main.pop()

    def get_min_stack(self):
        if len(self.stack_slave) != 0:
            return self.stack_slave[len(self.stack_slave) - 1]
        else:
            return None


min_stack = MinStack()
min_stack.en_stack(6)
min_stack.en_stack(7)
min_stack.en_stack(5)
print(min_stack.de_stack())
min_stack.en_stack(0)
print(min_stack.get_min_stack())

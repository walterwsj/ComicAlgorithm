class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self, node=None):
        self.root = node
        self.res = []

    def create_tree_by_list_2(self, data_list):
        node = TreeNode(data_list[0])
        if self.root is None:
            self.root = node
        index = 1
        len_list = len(data_list)
        stack = [self.root]
        while stack:
            tmp = stack.pop(0)
            if index == len_list:
                break
            if data_list[index] is not None:
                tmp.left_child = TreeNode(data_list[index])
            index += 1
            if index == len_list:
                break
            if data_list[index] is not None:
                tmp.right_child = TreeNode(data_list[index])
        return self.root

    def create_tree_by_list_1(self, data_list):
        self.root = TreeNode(data_list[0])
        index = 1
        node_list = [self.root]
        while node_list:
            tmp = node_list.pop(0)
            if index == len(data_list):
                break
            if data_list[index] is not None:
                tmp.left_child = TreeNode(data_list[index])
                node_list.append(tmp.left_child)
            index += 1
            if index == len(data_list):
                break
            if data_list[index] is not None:
                tmp.right_child = TreeNode(data_list[index])
                node_list.append(tmp.right_child)
        return self.root

    def create_tree_by_list(self, data_list):
        if data_list is None:
            return
        # 初始化根节点和一个标志位代表遍历元素的进度
        self.root = TreeNode(data_list[0])
        index = 1
        node_list = [self.root]
        while node_list:
            tmp = node_list.pop(0)
            if index == len(data_list):
                break
            if data_list[index] is not None:
                tmp.left_child = TreeNode(data_list[index])
                node_list.append(tmp.left_child)
            index += 1
            if index == len(data_list):
                break
            if data_list[index] is not None:
                tmp.right_child = TreeNode(data_list[index])
                node_list.append(tmp.right_child)
            index += 1
            if index == len(data_list):
                break
        return self.root

    def post_order_3(self, tree):
        stack, stack1 = [tree], []
        while stack:
            tmp = stack.pop()
            stack1.append(tmp)
            if tmp.left_child is not None:
                stack1.append(tmp.left_child)
            if tmp.right_child is not None:
                stack1.append(tmp.right_child)
        while stack1:
            self.res.append(stack1.pop().data)
        return self.res

    def in_order_non_recurse_1(self, tree):
        stack = []
        while tree or stack:
            while tree:
                stack.append(tree)
                tree = tree.left_child
            if stack:
                tmp = stack.pop()
                self.res.append(tmp.data)
                tree = tmp.right_child
        return self.res

    def in_order(self, tree):
        if tree is not None:
            self.res.append(tree.data)
        if tree.left_child is not None:
            self.in_order(tree.left_child)
        if tree.right_child is not None:
            self.in_order(tree.right_child)
        return self.res

    def pre_order(self, tree):
        if tree is not None:
            self.res.append(tree.data)
        if tree.left is not None:
            self.pre_order(tree.left_child)
        if tree.right is not None:
            self.pre_order(tree.right_child)
        return self.res

    def in_order_non_recurse(self, tree):
        stack = []
        while stack or tree:
            while tree:
                stack.append(tree)
                tree = tree.left_child
            if stack:
                tmp = stack.pop()
                self.res.append(tmp.data)
                tree = tmp.right_child
        return self.res

    def post_order_non_recurse(self, tree):
        stack1, stack2 = [tree], []
        while stack1:
            tmp = stack1.pop()
            stack2.append(tmp)
            if tmp.left_child is not None:
                stack1.append(tmp.left_child)
            if tmp.right_child is not None:
                stack1.append(tmp.right_child)
        while stack2:
            self.res.append(stack2.pop().data)
        return self.res

    def pre_order_no_recurse(self, tree):
        stack = []
        while stack or tree:
            while tree:
                self.res.append(tree.data)
                stack.append(tree)
                tree = tree.right_child
            if stack:
                tmp = stack.pop()
                tree = tmp.right_child
        return self.res

    def in_order_no_recurse(self, tree):
        stack = []
        while stack or tree:
            while tree:
                stack.append(tree)
                tree = tree.left_child
            if stack:
                tmp = stack.pop()
                self.res.append(tmp.data)
                tree = tmp.right_child
        return self.res

    def post_order_no_recurse(self, tree):
        stack1 = [tree]
        stack2 = []
        while stack1:
            tmp = stack1.pop()
            stack2.append(tmp)
            if tmp.left_child is not None:
                stack1.append(tmp.left_child)
            if tmp.right_child is not None:
                stack1.append(tmp.right_child)
        while stack2:
            self.res.append(stack2.pop().data)
        return self.res

    def bread_first_search(self, tree):
        my_queue = [tree]
        while my_queue:
            tmp = my_queue.pop(0)
            self.res.append(tmp.data)
            if tmp.left_child is not None:
                my_queue.append(tmp.left_child)
            if tmp.right_child is not None:
                my_queue.append(tmp.right_child)
        return self.res

    def breath_first_search(self, tree):
        queue = [tree]
        while queue:
            tmp = queue.pop(0)
            self.res.append(tmp.data)
            if tmp.left_child is not None:
                queue.append(tmp.left_child)
            if tmp.right_child is not None:
                queue.append(tmp.right_child)
        return self.res

    def bread_first_search_1(self, tree):
        queue = [tree]
        while queue:
            tmp = queue.pop(0)
            self.res.append(tmp.data)
            if tmp.left_child is not None:
                queue.append(tmp.left_child)
            if tmp.right_child is not None:
                queue.append(tmp.right_child)
        return self.res

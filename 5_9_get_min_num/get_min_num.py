def get_min_num(num, k):
    list_num = list(str(num))
    if k > len(list_num):
        return -1
    if k == len(list_num):
        return 0
    while k > 0:
        for i in range(1, len(list_num)):
            if list_num[i - 1] > list_num[i]:
                list_num.pop(i - 1)
                break
        k -= 1
    return list_num


def get_min_num_1(num, k):
    list_num = list(str(num))
    new_len = len(list_num) - k
    res = ["" for i in range(new_len)]
    top = 0
    for i in range(len(list_num)):
        while top > 0 and k > 0 and res[top - 1] > list_num[i]:
            top -= 1
            k -= 1
        res[top] = list_num[i]
        top += 1
    offset = 0
    while offset < new_len and res[offset] == '0':
        offset += 1
    if offset == new_len:
        return "0"
    else:
        res = res[offset:new_len - offset]
        return "".join(res)


def get_min_num_2(num, k):
    # 元素依次入栈。 判断三次当前数是否小于上一个数
    # 考虑零的位置 1.第一个 实数前为零的全部去掉 2.全是零 结果为零
    num_list = list(str(num))
    new_length = len(str(num)) - k
    stack = ["" for i in range(new_length)]
    top = 0
    offset = 0

    for i in num_list:
        while top > 0 and k > 0 and stack[top - 1] > i:
            top -= 1
            k -= 1
        stack[top] = i
        top += 1
    while offset < new_length and stack[offset] == '0':
        offset += 1
    if offset == new_length:
        return 0
    else:
        return stack[offset:new_length - offset]


def get_min_num_3(num, k):
    num_list = list(str(num))
    new_length = len(num_list) - k
    top = 0
    stack = [0 for i in range(new_length)]
    for i in num_list:
        while k > 0 and top > 0 and i < stack[top - 1]:
            top -= 1
            k -= 1
        stack[top] = i
        top += 1
    offset = 0
    while offset < new_length and stack[0] == 0:
        offset += 1
    if offset == new_length:
        return 0
    else:
        return stack[offset:new_length - offset]


def get_min_num_4(num, k):
    num_list = list(str(num))
    if len(num_list) < k:
        return None
    else:
        new_num_len = len(num_list) - k
        stack = [0 for i in range(new_num_len)]
        top = 0
        offset = 0
        for i in num_list:
            while top > 0 and k > 0 and int(i) < int(stack[top-1]):
                top -= 1
                k -= 1
            stack[top] = i
            top += 1
        while offset < new_num_len and int(stack[offset]) == 0:
            offset += 1
        if offset == new_num_len:
            return 0
        else:
            return ''.join([str(i) for i in stack[offset:new_num_len - offset + 1]])


a = 30200
print(get_min_num_4(a, 1))

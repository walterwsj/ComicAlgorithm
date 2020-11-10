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


a = 30200
print(get_min_num_1(a, 1))

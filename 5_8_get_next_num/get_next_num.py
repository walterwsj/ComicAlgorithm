# 一个数字全排列的下一个数
# 找到这个数字的有序区 12354
# 将无序区的第一个大于有序边界的数调换就是下一个刚刚大于原数的数字了
def get_next_num(num):
    num_list = list(str(num))
    border = -1
    tmp_min = -1
    for i in (range(1, len(num_list)))[::-1]:
        if num_list[i] > num_list[i - 1]:
            border = i
            break
    if border == -1:
        return -1
    else:
        if border == len(num_list) - 1:
            tmp_min = border - 1
        else:
            border -= 1
            for i in range(border + 1, len(num_list)):
                tmp_min = i
                if num_list[tmp_min] > num_list[i]:
                    tmp_min = i
    num_list[border], num_list[tmp_min] = num_list[tmp_min], num_list[border]
    return num_list


def get_next_num_1(num):
    num = list(str(num))
    # 1 get border
    border = get_border(num)
    # 2 exchange the min value and border index
    num = exchange_list(num, border)
    # 3 sort the last part
    return sort_list(num, border)


def get_border(num):
    border = -1
    for i in range(1, len(num))[::-1]:
        if num[i] > num[i - 1]:
            border = i
            break
    return border


def exchange_list(num, border):
    tmp_min = -1
    border -= 1
    for i in range(border, len(num) - 1):
        tmp_min = i
        if num[tmp_min] > num[i + 1]:
            tmp_min = i + 1

    num[tmp_min], num[border] = num[border], num[tmp_min]
    return num


def sort_list(num, border):
    i = border
    j = len(num) - 1
    while i < len(num) and j > border:
        num[i], num[j] = num[j], num[i]
        i += 1
        j -= 1
    return num


def get_next_num_2(num):
    num = list(str(num))
    # 1 get border
    border = get_border_2(num)
    # 2 exchange the min value and border index
    num = exchange_list_2(num, border)
    # 3 sort the last part
    return sort_list_2(num, border)


def get_border_2(num_list):
    border = -1
    for i in range(1, len(num_list))[::-1]:
        if num_list[i] > num_list[i - 1]:
            border = i - 1
            break
    return border


def exchange_list_2(num_list, index):
    tmp_list = num_list[index:]
    min_index = 0
    for i in range(1, len(tmp_list)):
        if tmp_list[i] < tmp_list[min_index]:
            min_index = i
    num_list[index], num_list[min_index] = num_list[min_index], num_list[index]
    return num_list


def sort_list_2(num, border):
    i = len(num) - 1
    j = border
    while i > border and j < len(num) - 1:
        num[i], num[j] = num[j], num[i]
        i -= 1
        j += 1
    return num


def get_next_num_3(num):
    # Find the border which is reverse
    num_list = list(str(num))
    len_list = len(num_list)
    border = -1
    for i in range(len_list - 1, 0, -1):
        if num_list[i] > num_list[i - 1]:
            border = i - 1
            break

    # Exchange the smallest num with the border
    end = len(num_list)
    index = border+1
    for i in range(border + 2, end):
        if num_list[i] < num_list[index]:
            index = i
    num_list[index], num_list[border] = num_list[border], num_list[index]

    # Sort the desc part asc
    i = border + 1
    j = len_list-1
    while i < len_list and j > border:
        num_list[i], num_list[j] = num_list[j], num_list[i]
        i += 1
        j -= 1

    return ''.join(str(i) for i in num_list)


a = 12354
print(get_next_num_3(a))

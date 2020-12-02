def bubble_sort(num_list):
    border = len(num_list) - 1
    tmp_index = -1
    for i in range(len(num_list)):
        is_sorted = True
        for j in range(border):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                tmp_index = j
                is_sorted = False
        border = tmp_index
        if is_sorted:
            break
    return num_list


def get_pivot(unsorted_list, head, tail):
    border = head
    tmp = unsorted_list[head]

    for i in range(head + 1, tail + 1):
        if unsorted_list[i] < tmp:
            border += 1
            unsorted_list[border], unsorted_list[i] = unsorted_list[i], unsorted_list[border]

    if border != head:
        unsorted_list[border], unsorted_list[head] = unsorted_list[head], unsorted_list[border]
    return border


def quick_sort(test_list, left, right):
    if left >= right:
        return
    key = get_pivot(test_list, left, right)
    quick_sort(test_list, left, key - 1)
    quick_sort(test_list, key + 1, right)
    return test_list


def quick_sort_no_recurse(test_list, head, tail):
    index_dict = {"left": head, "right": tail}
    stack = [index_dict]
    while stack:
        tmp = stack.pop()
        key = get_pivot(test_list, tmp["left"], tmp["right"])
        if key - 1 > tmp["left"]:
            tmp["right"] = key - 1
            stack.append(tmp)
        if key + 1 < tmp["right"]:
            tmp["left"] = key + 1
            stack.append(tmp)
    return test_list


def heap_sort(num_list):
    for i in range((len(num_list) - 2) // 2)[::-1]:
        heap_build(num_list, i, len(num_list))
    for i in range(len(num_list))[::-1]:
        num_list[i], num_list[0] = num_list[0], num_list[i]
        heap_build(num_list, 0, i)
    return num_list


def heap_build(num_list, index, border):
    child_leaf = 2 * index + 1
    tmp = num_list[index]
    while child_leaf < border:
        if child_leaf + 1 < border and num_list[child_leaf + 1] > num_list[child_leaf]:
            child_leaf += 1
        if tmp > num_list[child_leaf]:
            break
        num_list[index] = num_list[child_leaf]
        index = child_leaf
        child_leaf = 2 * child_leaf + 1
    num_list[index] = tmp


def up_adjust(num_list):
    child_index = len(num_list) - 1
    parent_index = child_index // 2
    tmp = num_list[child_index]
    while child_index > 0 and num_list[parent_index] > tmp:
        num_list[child_index] = num_list[parent_index]
        child_index = parent_index
        parent_index = (parent_index - 1) // 2
    num_list[child_index] = tmp


def count_sort(num_list):
    max_num = num_list[0]
    min_num = num_list[0]
    for i in num_list:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i

    gap = max_num - min_num
    res = [0 for i in range(gap + 1)]
    for i in range(len(num_list)):
        res[num_list[i] - min_num] += 1

    for i in range(1, len(num_list) - 1):
        res[i] += res[i - 1]

    sorted_list = [0 for i in range(len(num_list))]

    for i in range(len(num_list))[::-1]:
        sorted_list[res[num_list[i] - min_num] - 1] = num_list[i]
        res[num_list[i] - min_num] -= 1

    return sorted_list


def count_sort_1(num_list):
    max_num = num_list[0]
    min_num = num_list[0]
    for i in num_list:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i

    gap = max_num - min_num + 1
    count_list = [0 for i in range(gap)]

    for i in range(len(num_list)):
        count_list[num_list[i] - min_num] += 1

    for i in range(1, len(count_list) - 1):
        count_list[i] += count_list[i - 1]

    res = [0 for i in range(len(num_list))]

    for i in range(len(num_list))[::-1]:
        res[count_list[num_list[i] - min_num] - 1] = num_list[i]
        count_list[num_list[i] - min_num] -= 1

    return res


def bucket_sort(num_list):
    max_num = num_list[0]
    min_num = num_list[0]
    for i in num_list:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i

    gap = max_num - min_num
    bucket_num = len(num_list)
    buckets = [[] for i in range(bucket_num)]
    for i in num_list:
        index = (i - min_num) * (bucket_num - 1) // gap
        buckets[index].append(i)

    for bucket in buckets:
        bubble_sort(bucket)

    res = [i for bucket in buckets for i in bucket]
    return res


def count_sort_2(num_list):
    max_num = num_list[0]
    min_num = num_list[0]
    for i in num_list:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i

    gap = max_num - min_num
    count_list = [0] * (gap + 1)
    for i in num_list:
        count_list[i - min_num] += 1
    for i in range(1, gap + 1):
        count_list[i] += count_list[i - 1]

    res = [0] * len(num_list)
    for i in range(len(num_list)):
        res[count_list[num_list[i] - min_num] - 1] = num_list[i]
        count_list[num_list[i] - min_num] -= 1
    return num_list


def heap_sort_1(num_list):
    len_list = len(num_list)
    for i in range(len_list // 2, -1, -1):
        heap_build_1(num_list, i, len_list)
    for i in range(len_list - 1, -1, -1):
        num_list[i], num_list[0] = num_list[0], num_list[i]
        heap_build_1(num_list, 0, i)
    return num_list


def heap_build_1(num_list, index, border):
    parent, child, tmp = index, 2 * index + 1, num_list[index]
    while child < border:
        if child + 1 < border and num_list[child] < num_list[child + 1]:
            child += 1
        if tmp > num_list[child]:
            break
        num_list[parent] = num_list[child]
        parent = child
        child = 2 * child + 1
    num_list[parent] = tmp


def bucket_sort_2(num_list):
    max_num = num_list[0]
    min_num = num_list[0]
    for i in num_list:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i

    gap = max_num - min_num
    bucket_num = len(num_list)
    buckets = [[]] * bucket_num
    for i in range(bucket_num):
        index = (num_list[i] - min_num) * gap / (bucket_num - 1)
        buckets[i].append(bucket_num[i])

    for bucket in buckets:
        bucket = sorted(bucket)

    return [j for bucket in buckets for j in bucket]


a = [5, 4, 3, 2, 2, 1]
print(bucket_sort(a))

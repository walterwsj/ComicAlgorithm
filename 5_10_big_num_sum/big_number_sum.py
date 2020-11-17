def get_big_numbers_sum(num_a, num_b):
    len_res = len(num_a) if len(num_a) > len(num_b) else len(num_b)
    res = [0 for i in range(len_res + 1)]
    list_a = [0 for i in range(len_res + 1)]
    list_b = [0 for i in range(len_res + 1)]
    for i in range(len(num_a))[::-1]:
        list_a[i] = int(num_a[len(num_a) - i - 1])
    for i in range(len(num_b))[::-1]:
        list_b[i] = int(num_b[len(num_b) - i - 1])
    for j in range(len_res + 1):
        res[j] += list_a[j]
        res[j] += list_b[j]
        if res[j] > 10:
            res[j] -= 10
            res[j + 1] = 1
    while True:
        if res[len(res) - 1] == 0:
            res.pop(len(res) - 1)
        else:
            break

    final = []
    for i in range(len_res)[::-1]:
        final.append(res[i])
    final = [str(i) for i in final]
    return ''.join(final)


def get_big_numbers_sum_1(num_a, num_b):
    a_len = len(str(num_a))
    b_len = len(str(num_b))
    res = a_len if a_len > b_len else b_len
    list_a = [0 for i in range(res + 1)]
    list_b = [0 for i in range(res + 1)]
    list_res = [0 for i in range(res + 1)]

    for i in range(res + 1):
        if a_len > 0:
            list_a[i] = int(str(num_a)[res - i - 1])
            a_len -= 1
        else:
            break

    for i in range(res + 1):
        if b_len > 0:
            list_b[i] = int(str(num_b)[res - i - 1])
            b_len -= 1
        else:
            break

    for k in range(res + 1):
        list_res[k] += list_a[k]
        list_res[k] += list_b[k]
        if list_res[k] >= 10:
            list_res[k] = list_res[k] - 10
            list_res[k + 1] = 1

    while True:
        if list_res[len(list_res) - 1] == 0:
            list_res.pop(len(list_res) - 1)
        else:
            break

    tmp_list = list_res[::-1]
    final_num = ''.join(str(i) for i in tmp_list)
    return final_num





a = "123"
b = "237"
print(get_big_numbers_sum_1(a, b))

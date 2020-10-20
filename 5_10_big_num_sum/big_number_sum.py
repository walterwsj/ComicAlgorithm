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


a = "123"
b = "234"
print(get_big_numbers_sum(a, b))

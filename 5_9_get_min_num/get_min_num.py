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


a = 19870
print(get_min_num(a, 5))

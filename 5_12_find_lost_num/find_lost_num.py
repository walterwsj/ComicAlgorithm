import random
from random import shuffle

"""
记住它只是起到乱序的功能！不能输出一个实在的列表！
就是将一个容器中的数据每次随机逐个遍历一遍
"""


def get_random_arr(test_list):
    shuffle(test_list)


def get_random_list(list_len):
    res = [i for i in range(1, list_len + 1)]
    for i in range(len(res))[::-1]:
        index = random.randint(0, i)
        res[i], res[index] = res[index], res[i]
    return res


def get_dup_num(test_list):
    base_list = [i for i in range(1, 11)]
    tmp_dict = {}
    for i in base_list:
        tmp_dict[str(i)] = i
    for j in test_list:
        if str(j) in tmp_dict.keys():
            tmp_dict.pop(str(j))
    res = [i for i in tmp_dict.values()][0]
    return res


def get_single_num(test_list):
    res = 0
    for i in range(0, len(test_list)):
        res ^= test_list[i]
    return res


def get_two_single_nums(test_list):
    res = [0, 0]
    tmp = 0
    for i in test_list:
        tmp ^= i
    if tmp == 0:
        return None
    sep_pos = 1
    while tmp & sep_pos == 0:
        sep_pos <<= 1
    for i in test_list:
        if i & sep_pos == 1:
            res[0] ^= i
        else:
            res[1] ^= i
    return res[0], res[1]


a = [1, 1, 2, 3, 4, 4]
print(get_two_single_nums(a))

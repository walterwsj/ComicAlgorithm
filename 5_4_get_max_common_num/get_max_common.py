def get_max_common(num_a, num_b):
    max_num = num_a if num_a > num_b else num_b
    min_num = num_a if num_a < num_b else num_b
    if max_num % min_num == 0:
        return min_num
    return get_max_common(max_num % min_num, min_num)


def get_max_common_1(num_a, num_b):
    if num_a == num_b:
        return num_a

    if num_a % 2 == 0 and num_b % 2 == 0:
        num_a >>= 1
        num_b >>= 1
        return get_max_common_1(num_a, num_b) << 1
    elif num_a % 2 == 0 and num_b % 2 != 0:
        num_a >>= 1
        return get_max_common_1(num_a, num_b)
    elif num_a % 2 != 0 and num_b % 2 == 0:
        num_b >>=1
        return get_max_common_1(num_a, num_b)
    else:
        max_num = num_a if num_a > num_b else num_b
        min_num = num_a if num_a < num_b else num_b
        return get_max_common_1(max_num - min_num, min_num)


print(get_max_common_1(64, 36))

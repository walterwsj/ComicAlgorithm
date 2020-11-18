from functools import reduce


def reverse_1(test_string):
    return ''.join(test_string[::-1])


def reverse_2(test_string):
    tmp_list = list(test_string)
    tmp_list.reverse()
    return ''.join(tmp_list)


def reverse_3(test_string):
    return reduce(lambda x, y: y + x, test_string)


def reverse_4(test_string):
    if len(test_string) < 1:
        return test_string
    return reverse_4(test_string[1:]) + test_string[0]


def reverse_5(test_string):
    list_string = list(test_string)
    i = 0
    j = len(list_string) - 1
    mid = len(list_string) // 2
    while i < mid <= j:
        list_string[i], list_string[j] = list_string[j], list_string[i]
        i += 1
        j -= 1
    return ''.join(list_string)


def reverse_6(test_string):
    return test_string[::-1]


def reverse_7(test_string):
    return reduce(lambda x, y: y + x, test_string)


def reverse_8(test_string):
    str_list = list(test_string)
    str_list.reverse()
    return "".join(str_list)


def reverse_9(test_string):
    if len(test_string) < 1:
        return test_string
    return reverse_9(test_string[1:]) + test_string[0]


xx = "cba96cba"
print(reverse_9(xx))

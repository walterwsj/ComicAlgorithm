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
    mid = len(list_string)//2
    while i < mid <= j:
        list_string[i], list_string[j] = list_string[j], list_string[i]
        i += 1
        j -= 1
    return ''.join(list_string)


xx = "cba69cba"
print(reverse_5(xx))

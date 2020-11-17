def is_multiple_of_2(num):
    return num & (num - 1) == 0


a = 1023
print(is_multiple_of_2(a))

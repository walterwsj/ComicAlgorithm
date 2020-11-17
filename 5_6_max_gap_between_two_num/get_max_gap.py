class MyBucket:
    def __init__(self):
        self.min_value = None
        self.max_value = None


def get_max_gap(num_list):
    max_value = num_list[0]
    min_value = num_list[1]
    for i in range(1, len(num_list)):
        if max_value < num_list[i]:
            max_value = num_list[i]
        if min_value > num_list[i]:
            min_value = num_list[i]

    gap = max_value - min_value
    res = [0 for i in range(gap + 1)]
    for i in range(len(num_list)):
        res[num_list[i] - min_value] += 1
    count = 0
    max_gap = 0
    for i in res:
        if i == 0:
            count += 1
            if count > max_gap:
                max_gap = count
        else:
            count = 0
    return max_gap


def get_max_gap_1(num_list):
    max_value = num_list[0]
    min_value = num_list[0]
    for i in range(1, len(num_list)):
        if max_value < num_list[i]:
            max_value = num_list[i]
        if min_value > num_list[i]:
            min_value = num_list[i]

    gap = max_value - min_value

    bucket_num = len(num_list)
    buckets = []
    for i in range(bucket_num):
        buckets.append(MyBucket())

    for i in num_list:
        index = int((i - min_value) * (bucket_num - 1) / gap)
        if buckets[index].min_value is None or buckets[index].min_value > i:
            buckets[index].min_value = i
        if buckets[index].max_value is None or buckets[index].max_value < i:
            buckets[index].max_value = i

    left_max = buckets[0].max_value
    max_distance = 0
    for i in range(1, len(buckets)):
        if buckets[i].min_value is None:
            continue
        if max_distance < buckets[i].min_value - left_max:
            max_distance = buckets[i].min_value - left_max
        left_max = buckets[i].min_value
    return max_distance


def get_max_gap_2(num_list):
    max_value = num_list[0]
    min_value = num_list[0]
    for i in range(1, len(num_list)):
        if max_value < num_list[i]:
            max_value = num_list[i]
        if min_value > num_list[i]:
            min_value = num_list[i]

    gap = max_value - min_value
    bucket_num = len(num_list)
    buckets = []
    for i in range(bucket_num):
        buckets.append(MyBucket())

    for i in num_list:
        index = int((i - min_value) * (bucket_num - 1) / gap)
        if buckets[index].min_value is None or buckets[index].min_value > i:
            buckets[index].min_value = i
        if buckets[index].max_value is None or buckets[index].max_value > i:
            buckets[index].max_value = i

    left_max = buckets[0].max_value
    max_distance = 0
    for i in range(bucket_num):
        if buckets[i].min_value is None:
            continue
        if max_distance < buckets[i].min_value - left_max:
            max_distance = buckets[i].min_value - left_max
        left_max = buckets[i].min_value
        return max_distance






a = [2, 6, 3, 4, 5, 10, 9]
print(get_max_gap_1(a))

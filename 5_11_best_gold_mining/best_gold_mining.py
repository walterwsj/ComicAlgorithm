# 动态规划
"""
n:金矿的数量 w:工人的数量 g[]:每个矿的收益 p[]:每个矿需要的工人
金矿数量为0 或者工人数量为0
F(n,w)=0 (n=0 or w=0)
当前工人数量不足以开采当前的金矿
F(n,w)=F(n-1,w) (n>=1,w<p[n-1])
常规情况 金矿的数量和工人的数量都有富余
F(n,w)=max(F(n-1,w),F(n-1,w-p[n-1])+g[n-1])
"""


def get_best_gold_mining_1(workers, worker_counts, gold_capacity):
    table_rows = len(worker_counts) + 1
    res = [[0 for i in range(workers + 1)] for j in range(table_rows)]
    for i in range(1, table_rows):
        for j in range(1, workers + 1):
            if j < worker_counts[i - 1]:
                res[i][j] = res[i - 1][j]
            else:
                res[i][j] = max(res[i - 1][j], res[i - 1][j - worker_counts[i - 1]] + gold_capacity[i - 1])
    return res[table_rows - 1][workers]


def get_best_gold_mining_2(workers, worker_counts, gold_capacity):
    res = [0 for i in range(workers + 1)]
    for i in range(1, len(gold_capacity) + 1):
        for j in range(1, workers + 1)[::-1]:
            if j >= worker_counts[i - 1]:
                res[j] = max(res[j], res[j - worker_counts[i - 1]] + gold_capacity[i - 1])
    return res[workers]


def get_best_gold_mining(workers, golds, gold_workers, gold_values):
    if workers == 0 or golds == 0:
        return 0
    if workers < gold_workers[golds - 1]:
        return get_best_gold_mining(workers, golds - 1, gold_workers, gold_values)
    return max(get_best_gold_mining(workers, golds - 1, gold_workers, gold_values),
               get_best_gold_mining(workers - gold_workers[golds - 1], golds - 1, gold_workers, gold_values) +
               gold_values[golds - 1])


def get_best_gold_mining_3(workers, worker_list, gold_list):
    rows = len(worker_list) + 1
    table = [[0 for i in range(workers + 1)] for j in range(rows)]
    for i in range(1, rows):
        for j in range(1, workers + 1):
            if j < worker_list[i - 1]:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(table[i - 1][j], table[i - 1][j - worker_list[i - 1]] + gold_list[i - 1])
    return table[rows - 1][workers]


def get_best_gold_mining_4(workers, work_list, gold_list):
    rows = len(work_list) + 1
    table = [[0 for i in range(workers + 1)] for i in range(rows)]
    for i in range(1, rows):
        for j in range(1, workers + 1):
            if work_list[i] > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(table[i - 1][j], table[i - 1][j - workers[i - 1]] + gold_list[i - 1])
    return table[rows - 1][workers]


def get_best_gold_mining_5(works, work_list, gold_list):
    res = [0 for i in range(works + 1)]
    for i in range(1, len(work_list) + 1):
        for j in range(1, works + 1)[::-1]:
            if work_list[i - 1] <= j:
                res[j] = max(res[j], res[j - work_list[i - 1]] + gold_list[i - 1])
    return res[works]


def get_best_gold_mining_6(workers, work_list, gold_list):
    # F(n,k)=F(n-1,k)
    rows = len(work_list) + 1
    table = [[0 for i in range(workers + 1)] for i in range(rows)]
    for i in range(1, rows):
        for j in range(1, workers):
            if j < work_list[i - 1]:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(table[i - 1][j], table[i - 1][j - work_list[i - 1]] + gold_list[i - 1])
    return table[rows - 1][workers]


def get_best_gold_mining_7(workers, work_list, gold_list):
    res = [0 for i in range(workers + 1)]
    for i in range(1, len(work_list) + 1):
        for j in range(1, len(workers) + 1)[::-1]:
            if j >= work_list[i - 1]:
                res[j] = max(res[j], res[j - work_list[i - 1]] + gold_list[i - 1])
    return res[workers]


def get_best_gold_mining_8(workers, mining_count, worker_list, gold_list):
    if workers == 0 or mining_count == 0:
        return 0
    if workers < worker_list[mining_count - 1]:
        return get_best_gold_mining_8(workers, mining_count - 1, worker_list, gold_list)
    return max(get_best_gold_mining_8(workers, mining_count - 1, worker_list, gold_list),
               get_best_gold_mining_8(workers - worker_list[mining_count - 1], mining_count - 1, worker_list,
                                      gold_list) + gold_list[mining_count - 1])


def get_best_gold_mining_9(workers, work_list, gold_list):
    rows = workers + 1
    table = [[i for i in range(rows)] for i in range(len(work_list) + 1)]
    for i in range(1, len(work_list)):
        for j in range(1, workers):
            if workers < j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(table[i - 1][j], table[i - 1][j - work_list[i - 1]] + gold_list[i - 1])
    return table[workers][len(work_list)]


def get_best_gold_mining_10(workers, work_list, gold_list):
    res = [0 for i in range(workers + 1)]
    for i in range(1, len(work_list)):
        for j in range(1, workers + 1)[::-1]:
            if j >= work_list[i - 1]:
                res[j] = max(res[j], res[j - work_list[i - 1]] + gold_list[i - 1])
    return res[workers]


def get_best_gold_mining_11(workers, golds, work_list, gold_list):
    if workers == 0 or golds == 0:
        return 0
    if workers < work_list[golds - 1]:
        return get_best_gold_mining_11(workers, golds - 1, work_list, gold_list)
    return max(get_best_gold_mining_11(workers, golds - 1, work_list, gold_list),
               get_best_gold_mining_11(workers - work_list[golds - 1], golds - 1, work_list, gold_list) + gold_list[
                   golds - 1])


def get_best_gold_mining_12(workers, work_list, gold_list):
    rows = len(work_list) + 1
    table = [[i for i in range(workers + 1)] for i in range(rows)]
    for i in range(1, rows):
        for j in range(1, workers + 1):
            if j < work_list[i - 1]:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(table[i - 1][j], table[i - 1][j - work_list[i - 1]] + gold_list[i - 1])
    return table[rows - 1][workers]


def get_best_gold_mining_13(workers, golds, work_list, gold_list):
    if workers <= 0 or golds <= 0:
        return 0
    if workers < work_list[golds - 1]:
        return get_best_gold_mining_13(workers, golds - 1, work_list, gold_list)
    return max(get_best_gold_mining_13(workers, golds - 1, work_list, gold_list),
               get_best_gold_mining_13(workers - work_list[golds - 1], golds - 1, work_list, gold_list) + gold_list[
                   golds - 1])


def get_best_gold_mining_14(workers, work_list, gold_list):
    cols = workers + 1
    rows = len(work_list) + 1
    res = [[i for i in range(cols)]] * rows
    for i in range(1, rows):
        for j in range(1, cols):
            if j < work_list[i - 1]:
                res[i][j] = res[i - 1][j]
            else:
                res[i][j] = max(res[i - 1][j], res[i - 1][j - work_list[i - 1]] + gold_list[i - 1])
    return res[rows - 1][cols - 1]


def get_best_gold_mining_15(workers, work_list, gold_list):
    rows = len(work_list) + 1
    cols = workers + 1
    res = [[i for i in range(cols)] * rows]
    for i in range(1, cols):
        for j in range(1, cols):
            if work_list[i - 1] > j:
                res[i][j] = res[i - 1][j]
            else:
                res[i][j] = max(res[i - 1][j], res[i - 1][j - work_list[i - 1]] + gold_list[i - 1])
    return res[rows - 1][cols - 1]


def get_best_gold_mining_16(workers, golds, work_list, gold_list):
    if workers == 0 or golds == 0:
        return 0
    if workers < work_list[golds - 1]:
        return get_best_gold_mining_16(workers, golds - 1, work_list, gold_list)
    else:
        return max(get_best_gold_mining_16(workers, golds - 1, work_list, gold_list),
                   get_best_gold_mining_16(workers - work_list[golds - 1], golds - 1, work_list, gold_list) +
                   gold_list[golds - 1])


def get_best_gold_mining_17(workers, work_list, gold_list):
    res = [i for i in range(workers + 1)]
    for i in range(1, len(work_list) + 1):
        for j in range(workers, -1, -1):
            if j > work_list[i]:
                res[j] = max(res[j], res[j - work_list[i - 1]] + gold_list[i - 1])
    return res[workers]


def get_best_gold_mining_18(workers, work_list, gold_list):
    len_work_list = len(work_list) + 1
    res = [i for i in range(workers + 1)]
    for i in range(1, len_work_list):
        for j in range(workers, -1, -1):
            if j > work_list[i]:
                res[j] = max(res[j], res[j - work_list[i - 1]] + gold_list[i - 1])
    pass


w = 10
p = [5, 5, 3, 4, 3]
g = [400, 500, 200, 300, 350]
print(get_best_gold_mining_12(10, p, g))

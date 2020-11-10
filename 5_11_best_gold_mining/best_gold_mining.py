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


w = 10
p = [5, 5, 3, 4, 3]
g = [400, 500, 200, 300, 350]
print(get_best_gold_mining_5(10, p, g))

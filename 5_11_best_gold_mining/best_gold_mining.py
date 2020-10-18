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


def get_best_gold_mining(w, n, g, p):
    if n == 0 or w == 0:
        return 0
    if w < p[n - 1]:
        get_best_gold_mining(w, n - 1, g, p)
    return max(get_best_gold_mining(w, n - 1, g, p), get_best_gold_mining(w - p[n - 1], n - 1, g, p) + g[n - 1])


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
        for j in range(1, workers+1)[::-1]:
            if j >= worker_counts[i-1]:
                res[j] = max(res[j], res[j - worker_counts[i - 1]] + gold_capacity[i - 1])
    return res[workers]


w = 10
p = [5, 5, 3, 4, 3]
g = [400, 500, 200, 300, 350]
print(get_best_gold_mining_2(w, p, g))

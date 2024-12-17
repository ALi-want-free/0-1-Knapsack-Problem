def knapsack_01(weights, values, capacity):
    """
    解决 0/1 背包问题的动态规划方法
    
    :param weights: 物品的重量列表
    :param values: 物品的价值列表
    :param capacity: 背包的最大容量
    :return: 背包能装入物品的最大价值
    """
    n = len(weights)  # 物品数量
    
    # 初始化 DP 表格，(n+1) * (capacity+1)，初始值为0
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # 填充 DP 表格
    for i in range(1, n + 1):  # 遍历物品
        for w in range(1, capacity + 1):  # 遍历容量
            if weights[i - 1] <= w:  # 当前物品可以放入背包
                # 选择放入当前物品或者不放入，取价值较大的情况
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # 当前物品无法放入，继承上一个状态
                dp[i][w] = dp[i - 1][w]
    
    # 返回 DP 表的最后一个元素，即为最大价值
    return dp[n][capacity]

# 测试用例
if __name__ == "__main__":
    weights = [2, 3, 4, 5]  # 物品的重量
    values = [3, 4, 5, 6]   # 物品的价值
    capacity = 8            # 背包容量
    
    max_value = knapsack_01(weights, values, capacity)
    print(f"0/1 背包问题的最大价值为: {max_value}")

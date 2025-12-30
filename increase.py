from scipy.stats import linregress
import numpy as np


def check_trend_statistical(y, alpha=0.05):
    """
    用线性回归判断三个数的趋势是否显著
    参数：
        y: 三个数的列表或数组，如[1,3,5]
        alpha: 显著性水平（默认0.05）
    返回：
        趋势判断结果
    """
    if len(y) != 3:
        raise ValueError("输入必须是三个数")

    # x取1,2,3（代表三个数据点的顺序）
    x = np.array([0.1, 0.2, 0.3])
    # 线性回归
    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    # 判断趋势
    if p_value < alpha:
        if slope > 0:
            return f"显著上升趋势（斜率={slope:.2f}，p值={p_value:.4f} < {alpha}）"
        else:
            return f"显著下降趋势（斜率={slope:.2f}，p值={p_value:.4f} < {alpha}）"
    else:
        return f"无显著趋势（斜率={slope:.2f}，p值={p_value:.4f} ≥ {alpha}）"


# 测试示例
print(check_trend_statistical([0.815, 0.769, 0.538]))  # 显著上升
print(check_trend_statistical([5, 3, 1]))  # 显著下降
print(check_trend_statistical([1, 5, 3]))  # 无显著趋势
print(check_trend_statistical([2, 2.5, 3]))  # 显著上升（微弱但显著）
print(check_trend_statistical([3, 2.5, 2]))  # 显著下降（微弱但显著）
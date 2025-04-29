import numpy as np

"""
大角度单摆周期的数值积分计算（自适应梯形法则）

本程序用于实现自适应变步长梯形积分法，计算大角度单摆的周期，并分析大角度对单摆周期的影响。
主要功能包括：
1. 实现自适应梯形积分函数；
2. 计算不同最大摆角下的周期比值 T/T0；
3. 通过数值方法确定周期相对误差为5%时的临界角度。
"""

# 梯形积分法
def trapezoid(f, a, b, N):
    """
    梯形法数值积分
    :param f: 被积函数，单参数
    :param a: 积分下限
    :param b: 积分上限
    :param N: 子区间数
    :return: 积分近似值
    """
    h = (b - a) / N
    s = 0.5 * f(a) + 0.5 * f(b)
    for k in range(1, N):
        s += f(a + k * h)
    return h * s

# TODO: 实现自适应梯形积分函数
def adaptive_trapezoidal(f, a, b, tol=1e-5, n=5, N=10):
    """
    自适应变步长梯形积分法
    :param f: 被积函数，单参数
    :param a: 积分下限
    :param b: 积分上限
    :param tol: 相对误差容限
    :param n: 初始较小区间数
    :param N: 初始较大区间数
    :return: 积分近似值
    """
    # 请补充自适应梯形法的实现
    pass

# 单摆周期积分中的被积函数
def integrand(theta, theta0_rad):
    """
    单摆周期积分的被积函数
    :param theta: 当前积分变量
    :param theta0_rad: 最大摆角（弧度）
    :return: 被积函数值
    """
    return 1 / np.sqrt(1 - (np.sin(theta0_rad / 2)) ** 2 * (np.sin(theta)) ** 2)

# 计算周期比值 T/T0
def compute_period_ratio(theta0_deg, tol=1e-5):
    """
    计算给定最大摆角下的周期比值 T/T0
    :param theta0_deg: 最大摆角（度）
    :param tol: 积分精度
    :return: T/T0
    """
    theta0_rad = np.deg2rad(theta0_deg)
    f = lambda theta: integrand(theta, theta0_rad)
    # TODO: 调用自适应梯形法计算积分
    integral_result = None
    return (2 / np.pi) * integral_result if integral_result is not None else None

# 任务3：确定临界角度
def find_critical_angle(target_relative_error=0.05, tol=1e-5):
    """
    利用二分法等数值方法，确定使周期相对误差为5%的临界角度
    :param target_relative_error: 目标相对误差
    :param tol: 角度精度
    :return: 临界角度（度）
    """
    # TODO: 实现二分法或其他方法搜索临界角度
    pass

def main():
    """
    主函数：输出不同角度下的周期比值和临界角度
    """
    angles_deg = [1, 3, 5, 7, 10, 15, 20, 25]
    print("计算不同角度下单摆周期比值 T/T0：")
    for angle in angles_deg:
        ratio = compute_period_ratio(angle)
        print(f"θ0 = {angle}°, T/T0 = {ratio:.5f}" if ratio is not None else f"θ0 = {angle}°, T/T0 = 未计算")

    critical_angle = find_critical_angle()
    print("\n周期相对误差达到5%时的临界角度为：")
    print(f"θ0 ≈ {critical_angle:.5f}°" if critical_angle is not None else "θ0 未计算")

if __name__ == "__main__":
    main()
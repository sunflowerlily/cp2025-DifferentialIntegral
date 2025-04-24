import numpy as np
import matplotlib.pyplot as plt
from sympy import tanh, symbols, diff, lambdify

def get_analytical_derivative():
    """获取解析导数函数"""
    x = symbols('x')
    expr = diff(1+0.5*tanh(2*x),x)
    return lambdify(x, expr)

def f(x):
    """原始函数"""
    return 1+0.5*np.tanh(2*x)

def calculate_central_difference(x, f):
    """使用中心差分法计算数值导数"""
    dy = []
    dx = x[2]-x[0]
    for i in range(1, len(x)-1):
        dy.append((f(x[i+1])-f(x[i-1]))/dx)
    return np.array(dy)

def richardson_derivative(x, f, h, n=1):
    """使用Richardson外推法计算导数，支持任意阶外推
    
    参数:
    x: 计算导数的点
    f: 要求导的函数
    h: 初始步长
    n: 外推阶数（默认为1阶）
    
    返回:
    导数值
    """
    # 创建Richardson表
    R = np.zeros((n+1, n+1))
    
    # 计算第一列（不同步长的中心差分）
    for i in range(n+1):
        hi = h / (2**i)
        R[i,0] = (f(x + hi) - f(x - hi)) / (2 * hi)
    
    # Richardson外推
    for j in range(1, n+1):
        for i in range(n-j+1):
            R[i,j] = (4**j * R[i+1,j-1] - R[i,j-1]) / (4**j - 1)
    
    return R[0,n]

def create_comparison_plot():
    """创建对比图，同时显示中心差分和Richardson外推的结果"""
    N = 50
    x = np.linspace(-2, 2, N)
    
    # 创建图形，添加第三个子图
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12), height_ratios=[3, 1, 1], sharex=True)
    
    # 获取解析导数
    df = get_analytical_derivative()
    
    # 计算中心差分导数
    dy_central = calculate_central_difference(x, f)
    x_central = x[1:-1]
    
    # 计算不同阶数的Richardson外推导数
    dy_richardson_1 = np.array([richardson_derivative(xi, f, 0.1, n=1) for xi in x])
    dy_richardson_2 = np.array([richardson_derivative(xi, f, 0.1, n=2) for xi in x])
    dy_richardson_3 = np.array([richardson_derivative(xi, f, 0.1, n=3) for xi in x])
    
    # 绘制第一个子图：导数比较
    ax1.plot(x, df(x), 'b-', label='Analytical Solution')
    ax1.plot(x_central, dy_central, 'ro', label='Central Difference', markersize=4)
    ax1.plot(x, dy_richardson_2, 'g^', label='Richardson Solution', markersize=4)
    ax1.set_title('Derivative Comparison')
    ax1.set_ylabel('dy/dx')
    ax1.legend()
    ax1.grid(True)
    
    # 计算并绘制第二个子图：中心差分和Richardson外推的误差对比
    analytical_central = df(x_central)
    analytical_richardson = df(x)
    difference_central = dy_central - analytical_central
    difference_richardson = dy_richardson_2 - analytical_richardson
    
    ax2.plot(x_central, difference_central, 'ro', label='Central Difference Error', markersize=4)
    ax2.plot(x, difference_richardson, 'g^', label='Richardson Error', markersize=4)
    ax2.set_ylabel('error')
    ax2.legend()
    ax2.grid(True)
    
    # 绘制第三个子图：不同阶数Richardson外推的误差对比
    difference_r1 = dy_richardson_1 - analytical_richardson
    difference_r2 = dy_richardson_2 - analytical_richardson
    difference_r3 = dy_richardson_3 - analytical_richardson
    
    ax3.plot(x, difference_r1, 'r^', label='1st Order', markersize=4)
    ax3.plot(x, difference_r2, 'g^', label='2nd Order', markersize=4)
    ax3.plot(x, difference_r3, 'b^', label='3rd Order', markersize=4)
    ax3.set_xlabel('x')
    ax3.set_ylabel('Richardson Error')
    ax3.legend()
    ax3.grid(True)
    
    # 调整布局
    plt.subplots_adjust(hspace=0)
    
    plt.show()

if __name__ == '__main__':
    # 展示对比结果
    print("对比中心差分法和不同阶数的Richardson外推法...")
    create_comparison_plot()
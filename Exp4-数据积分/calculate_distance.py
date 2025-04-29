import numpy as np
from scipy.integrate import cumulative_trapezoid
import matplotlib.pyplot as plt

def main():
    # 1. 读取数据文件
    data = np.loadtxt('data/velocities.txt')
    t = data[:, 0]  # 时间列
    v = data[:, 1]   # 速度列

    # 2. 计算总距离
    total_distance = np.trapz(v, t)
    print(f"总运行距离: {total_distance:.2f} 米")

    # 3. 计算累积距离
    distance = cumulative_trapezoid(v, t, initial=0)

    # 4. 绘制图表
    plt.figure(figsize=(10, 6))
    
    # 绘制速度曲线
    plt.plot(t, v, 'b-', label='速度 (m/s)')
    
    # 绘制距离曲线
    plt.plot(t, distance, 'r--', label='距离 (m)')
    
    # 图表装饰
    plt.title('速度与距离随时间变化')
    plt.xlabel('时间 (秒)')
    plt.ylabel('速度 (米/秒) / 距离 (米)')
    plt.legend()
    plt.grid(True)
    
    # 显示图表
    plt.show()

if __name__ == '__main__':
    main()
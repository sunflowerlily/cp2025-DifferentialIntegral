import sys
import os
import numpy as np
import pytest

# 添加父目录到系统路径以导入被测试模块
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution.pendulum_period_solution import trapezoid, adaptive_trapezoidal, integrand, compute_period_ratio, find_critical_angle

class TestPendulumPeriodSolution:
    """测试大角度单摆周期数值解法"""

    def test_trapezoid_simple(self):
        """测试梯形法对简单函数的积分"""
        f = lambda x: x
        result = trapezoid(f, 0, 1, 100)
        assert abs(result - 0.5) < 1e-4

    def test_adaptive_trapezoidal_accuracy(self):
        """测试自适应梯形法对简单函数的精度"""
        f = lambda x: np.sin(x)
        result = adaptive_trapezoidal(f, 0, np.pi, tol=1e-6)
        assert abs(result - 2.0) < 1e-5

    def test_integrand_value(self):
        """测试被积函数在特定点的值"""
        theta0_rad = np.deg2rad(30)
        val = integrand(0, theta0_rad)
        assert abs(val - 1.0) < 1e-8

    def test_compute_period_ratio_small_angle(self):
        """小角度极限下T/T0应接近1"""
        ratio = compute_period_ratio(1)
        assert abs(ratio - 1.0) < 1e-3

    def test_compute_period_ratio_known(self):
        """测试几个已知角度下的T/T0"""
        # 这些值可通过高精度积分或文献查表获得
        test_angles = [10, 20, 30, 45]
        expected = [1.0017, 1.0068, 1.0151, 1.0356]
        for angle, exp_val in zip(test_angles, expected):
            ratio = compute_period_ratio(angle)
            assert abs(ratio - exp_val) < 0.01

    def test_find_critical_angle(self):
        """测试临界角度搜索功能"""
        angle = find_critical_angle(target_relative_error=0.05)
        # 5%误差对应角度约为20.7度（可查表或用精确解验证）
        assert 20 < angle < 22

if __name__ == "__main__":
    pytest.main([__file__])
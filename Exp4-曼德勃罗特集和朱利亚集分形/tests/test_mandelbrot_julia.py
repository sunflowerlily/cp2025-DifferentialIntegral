import unittest
import os
import sys
import numpy as np
from pathlib import Path

# 添加父目录到Python路径
sys.path.append(str(Path(__file__).parent.parent))

# 尝试导入学生代码，失败时导入参考解决方案
from mandelbrot_julia import generate_mandelbrot, generate_julia
#from solution.mandelbrot_julia_solution import generate_mandelbrot, generate_julia

class TestFractals(unittest.TestCase):
    def test_mandelbrot_shape(self):
        """测试Mandelbrot集输出形状"""
        result = generate_mandelbrot(width=400, height=300, max_iter=50)
        self.assertEqual(result.shape, (400, 300))
    
    def test_mandelbrot_values(self):
        """测试Mandelbrot集返回值范围"""
        result = generate_mandelbrot(width=100, height=100, max_iter=20)
        self.assertTrue(np.all(result >= 0))
        self.assertTrue(np.all(result <= 20))
        
    def test_julia_shape(self):
        """测试Julia集输出形状"""
        c = -0.8 + 0.156j
        result = generate_julia(c, width=300, height=400, max_iter=50)
        self.assertEqual(result.shape, (300, 400))
    
    def test_julia_values(self):
        """测试Julia集返回值范围"""
        c = 0.285 + 0.01j
        result = generate_julia(c, width=100, height=100, max_iter=30)
        self.assertTrue(np.all(result >= 0))
        self.assertTrue(np.all(result <= 30))
    
    def test_mandelbrot_edge_cases(self):
        """测试Mandelbrot集边界情况"""
        # 测试中心点(通常收敛)
        result = generate_mandelbrot(width=3, height=3, max_iter=100)
        self.assertGreater(result[1, 1], 90)  # 中心点通常不逃逸
        
        # 修改断言条件，检查左上角点是否快速逃逸
        self.assertLess(result[0, 0], 10)  # 左上角应该快速逃逸
    
    def test_julia_edge_cases(self):
        """测试Julia集边界情况"""
        c = -0.4 + 0.6j
        result = generate_julia(c, width=3, height=3, max_iter=50)
        # 至少有一个点应该快速逃逸
        self.assertTrue(np.any(result < 10))

if __name__ == "__main__":
    unittest.main()
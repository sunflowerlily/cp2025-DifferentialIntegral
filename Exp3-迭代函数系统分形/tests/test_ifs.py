import unittest
import os
import sys
from pathlib import Path
import numpy as np

# 添加父目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 导入学生代码或参考代码
from ifs import get_fern_params, get_tree_params, apply_transform, run_ifs
#from solution.ifs_solution import get_fern_params, get_tree_params, apply_transform, run_ifs

class TestIFS(unittest.TestCase):
    def test_fern_params(self):
        params = get_fern_params()
        self.assertIsInstance(params, list)
        self.assertEqual(len(params), 4)
        for p in params:
            self.assertEqual(len(p), 7)
    
    def test_tree_params(self):
        params = get_tree_params()
        self.assertIsInstance(params, list)
        self.assertEqual(len(params), 3)
        for p in params:
            self.assertEqual(len(p), 7)
    
    def test_apply_transform(self):
        point = (1, 1)
        params = [0.5, 0.3, -0.2, 0.4, 1.0, 0.5, 0.1]
        new_point = apply_transform(point, params)
        self.assertIsInstance(new_point, tuple)
        self.assertEqual(len(new_point), 2)
    
    def test_run_ifs_basic(self):
        # 测试简单IFS
        test_params = [
            [0.5, 0, 0, 0.5, 0, 0, 0.5],
            [0.5, 0, 0, 0.5, 1, 0, 0.5]
        ]
        points = run_ifs(test_params, num_points=1000)
        self.assertIsInstance(points, np.ndarray)
        self.assertEqual(points.shape, (1000, 2))
    
    def test_run_ifs_fern(self):
        fern_params = get_fern_params()
        points = run_ifs(fern_params, num_points=1000)
        self.assertIsInstance(points, np.ndarray)
        self.assertEqual(points.shape, (1000, 2))
    
    def test_run_ifs_tree(self):
        tree_params = get_tree_params()
        points = run_ifs(tree_params, num_points=1000)
        self.assertIsInstance(points, np.ndarray)
        self.assertEqual(points.shape, (1000, 2))

if __name__ == "__main__":
    unittest.main()
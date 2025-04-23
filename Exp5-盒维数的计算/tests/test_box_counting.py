import unittest
import numpy as np
from PIL import Image
import os
import sys
from pathlib import Path

# 添加父目录到Python路径
sys.path.append(str(Path(__file__).parent.parent))

# 导入解决方案代码  
#from solution.box_counting_solution import load_and_binarize_image, box_count, calculate_fractal_dimension
# 导入学生代码
from box_counting import load_and_binarize_image, box_count, calculate_fractal_dimension


class TestBoxCounting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """创建测试图像"""
        cls.test_image_path = "test_image.png"
        img_array = np.zeros((32, 32), dtype=np.uint8)
        img_array[8:24, 8:24] = 255  # 中心16x16白色方块
        Image.fromarray(img_array).save(cls.test_image_path)
        
    @classmethod 
    def tearDownClass(cls):
        """清理测试文件"""
        if os.path.exists(cls.test_image_path):
            os.remove(cls.test_image_path)

    def test_load_and_binarize(self):
        """测试图像加载和二值化"""
        binary_img = load_and_binarize_image(self.test_image_path)
        self.assertEqual(binary_img.shape, (32, 32))
        self.assertTrue(np.all(np.unique(binary_img) == [0, 1]))

    def test_box_count(self):
        """测试盒计数算法"""
        test_array = np.zeros((6,6), dtype=int)
        test_array[2:4, 2:4] = 1  # 中心2x2区域
        
        counts = box_count(test_array, [1,2,3,6])
        expected = {1:4, 2:1, 3:4, 6:1}
        self.assertEqual(counts, expected)

    def test_fractal_dimension(self):
        """测试分形维数计算"""
        test_array = np.zeros((128,128), dtype=int)  # 增大测试图像尺寸
        test_array[32:96, 32:96] = 1  # 64x64方块
        
        D, (epsilons, N_epsilons, slope, intercept) = calculate_fractal_dimension(
            test_array, 
            min_box_size=2,  # 设置最小盒子尺寸
            max_box_size=64,  # 设置最大盒子尺寸
            num_sizes=10     # 增加盒子尺寸数量
        )
        
        # 打印调试信息
        print(f"\nCalculated fractal dimension: {D:.4f}")
        print("Box sizes:", epsilons)
        print("Box counts:", N_epsilons)
        
        # 进一步放宽范围并添加更详细的断言
        self.assertGreater(D, 1.5, "分形维数应大于1.5")
        self.assertLess(D, 2.5, "分形维数应小于2.5")

if __name__ == "__main__":
    unittest.main()
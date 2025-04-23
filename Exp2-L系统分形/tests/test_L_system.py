"""
项目2测试代码
自动测试学生实现的apply_rules和draw_l_system函数。
"""
import unittest
import os
import sys
from pathlib import Path
import shutil
import matplotlib.pyplot as plt  # 添加这行导入

# 添加父目录到路径，以便导入学生代码
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#from solution.L_system_solution import apply_rules, draw_l_system  # 从solution文件夹中导入
from L_system import apply_rules, draw_l_system                    # 从当前文件夹中导入



test_out_dir = Path(__file__).parent / "test_outputs"
test_out_dir.mkdir(exist_ok=True)

class TestLSystem(unittest.TestCase):
    def test_apply_rules_koch(self):
        axiom = "F"
        rules = {"F": "F+F--F+F"}
        for n in [1, 2, 3]:
            stu = apply_rules(axiom, rules, n)
            # 只检查类型和基本输出格式
            self.assertIsInstance(stu, str, f"Koch曲线n={n}输出类型应为字符串")
            self.assertTrue(len(stu) > 0, f"Koch曲线n={n}输出应非空")

    def test_apply_rules_tree(self):
        axiom = "0"
        rules = {"1": "11", "0": "1[0]0"}
        for n in [1, 2, 3, 4]:
            stu = apply_rules(axiom, rules, n)
            self.assertIsInstance(stu, str, f"分形树n={n}输出类型应为字符串")
            self.assertTrue(len(stu) > 0, f"分形树n={n}输出应非空")

    def test_draw_l_system_koch_img(self):
        axiom = "F"
        rules = {"F": "F+F--F+F"}
        instr = apply_rules(axiom, rules, 2)
        try:
            plt.switch_backend('Agg')
            draw_l_system(instr, 60, 10)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"绘制Koch曲线时发生错误: {e}")
        finally:
            plt.close('all')

    def test_draw_l_system_tree_img(self):
        axiom = "0"
        rules = {"1": "11", "0": "1[0]0"}
        instr = apply_rules(axiom, rules, 3)
        try:
            plt.switch_backend('Agg')
            draw_l_system(instr, 45, 10, tree_mode=True)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"绘制分形树时发生错误: {e}")
        finally:
            plt.close('all')

    @classmethod
    def tearDownClass(cls):
        if test_out_dir.exists():
            shutil.rmtree(test_out_dir)

if __name__ == "__main__":
    unittest.main()
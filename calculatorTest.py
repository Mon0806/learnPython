# !/usr/bin/env python
# coding:utf-8

import unittest  # 使用unittest测试框架必须先import unittest类
from Calculator import calculator  # 引入被测试类


class calculatorTest(unittest.TestCase):  # unittest的测试类参数必须为unittest.TestCase

    def setUp(self):
        # print("Test start!")
        pass

    def test_base(self):
        j = calculator(4, 2)  # 先定义一个self.a = 4和self.b = 2的类变量j
        self.assertEqual(j.myadd(), 6)  # 通过断言函数验证计算结果与预期结果是否一致
        self.assertEqual(j.mysubs(), 2)
        self.assertEqual(j.mymultiply(), 8)
        self.assertEqual(j.mydivide(), 2)

    def test_divide(self):  # 对被除数为0的情况进行测试
        j = calculator(4, 0)
        self.assertEqual(j.mydivide(), 9999999999999999)

    def tearDown(self):
        # print("Test end!")
        pass


if __name__ == '__main__':  # 主函数
    # 构造测试集
    suite = unittest.TestSuite()
    # 把两个测试函数加进去
    suite.addTest(calculatorTest("test_base"))
    suite.addTest(calculatorTest("test_divide"))
    # 运行测试集合
    runner = unittest.TextTestRunner()
    runner.run(suite)
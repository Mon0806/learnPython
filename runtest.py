# !/usr/bin/env python
# coding:utf-8

import unittest
from HTMLTestRunner import HTMLTestRunner

test_dir = './'  # 定义测试文件的路径，这里为当前路径
# 调用测试路径下以Test结尾的.py文件
discover = unittest.defaultTestLoader.discover(test_dir, pattern="*Test.py")

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # 以下用于生成测试报告
    fp = open("result.html", "wb")
    runner = HTMLTestRunner(stream = fp, title = "测试报告", description = "测试用例执行报告")
    runner.run(discover)
    fp.close()



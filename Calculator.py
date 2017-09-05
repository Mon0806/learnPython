# !/usr/bin/env python
# coding:utf-8


class calculator:

    def __init__(self, a, b):  # 两个成员变量
        self.a = int(a)
        self.b = int(b)

    def myadd(self):  # 加法
        return self.a + self.b

    def mysubs(self):  # 减法
        return self.a - self.b

    def mymultiply(self):  # 乘法
        return self.a * self.b

    def mydivide(self):  # 除法
        try:
            return self.a/self.b
        except ZeroDivisionError:  # 若除数为0，返回一个很大的数
            print("除数不能为零")
            return 9999999999999999

import unittest
from HTMLTestRunner import  HTMLTestRunner

suite = unittest.TestSuite()
tests = unittest.defaultTestLoader.discover(r"G:\PycharmProjects\day17",pattern="Test*.py")
suite.addTests(tests)
f = open(file="测试报告.html",mode="w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream= f ,
    title="计算器测试报告",
    verbosity=1,
    description="执行了加减乘除用例测试"
)

runner.run(suite)

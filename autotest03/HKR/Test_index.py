from HTMLTestRunner import HTMLTestRunner
import unittest

suite = unittest.TestSuite()
tests = unittest.defaultTestLoader.discover(r"G:\PycharmProjects\自动化day03\HKR", pattern ="test_logic.py")
suite.addTests(tests)
f = open(file="测试报告.html",mode="w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream= f ,
    title="HKR测试报告",
    verbosity=3,
    description="执行了登陆测试"
)

runner.run(suite)
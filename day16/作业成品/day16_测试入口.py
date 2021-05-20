from HTMLTestRunner import  HTMLTestRunner
import unittest
import time
# 创建测试集
suite = unittest.TestSuite()
# 测试加载器加载测试用例
tests = unittest.defaultTestLoader.discover(r"G:\PycharmProjects\day16\作业成品",pattern="Test*.py")
# 将用例放入测试集
suite.addTests(tests)
# 创建测试运行器
f = open(file="测试报告.html",mode="w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    #报告标题
    title = "对 类方法工具化数据库银行 的测试报告",
    #详细级别.1运行时显示为点.2为执行某一项的进度 默认参数为1
    verbosity = 1,
    #执行备注
    description= "执行了 新增/存钱/取钱/转账 用例"
)

runner.run(suite)
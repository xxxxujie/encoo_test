# 1、收集项目中所有的测试用例
import unittest

import unittestreport

tests = unittest.defaultTestLoader.discover('tests')

# 4、使用定制的运行器，安装能带有额外功能的运行器，比如生成html报告
runner = unittestreport.TestRunner(
    tests,
    filename='output.html',
    title='encoo测试报告',
    tester='xu',
    desc='描述。。。',
    templates=2
)

runner.run()
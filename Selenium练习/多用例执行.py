#！/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

# 定义测试用例的目录为当前目录中test_case/目录
test_dir = '.'
suits = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suits)
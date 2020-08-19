#!/use/bin/env python
#coding:utf-8 

#Author:WuYa

import  unittest
from base.method import Method,IsAssert

class LaGou(unittest.TestCase):
	def setUp(self):
		self.obj=Method()
		self.p=IsAssert()

	def statusCode(self,r):
		self.assertEqual(r.status_code, 200)
		self.assertEqual(r.json()['code'], 0)

	def test_laGou_001(self):
		'''拉钩:测试翻页'''
		r=self.obj.post(1)
		self.statusCode(r=r)
		self.assertTrue(self.p.isContent(1,r.text))

if __name__ == '__main__':
    unittest.main(verbosity=2)

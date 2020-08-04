import csv
import codecs
import unittest
from time import sleep
from itertools import islice
from selenium import webdriver


class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(3)

    def test_search(self):
        #codecs模块为我们解决的字符编码的处理提供了lookup方法，它接受一个字符编码名称的参数，并返回指定字符编码对应的 encoder、decoder、StreamReader和StreamWriter的函数对象和类对象的引用。
        with codecs.open('baidu_data.csv', 'r', 'utf_8_sig') as f:
            data = csv.reader(f)    #csv.reader()返回一个reader对象，利用该对象遍历csv文件中的行。此处读取到的数据是将每行数据当做列表返回的。
            for line in islice(data, 1, None):  #从第二行开始迭代（不读取文件第一行）
                search_key = line[1]        #传第二列的值
                self.baidu_search(search_key)


if __name__ == '__main__':
    unittest.main(verbosity=2)

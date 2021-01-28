import unittest #builtin library
from selenium import  webdriver
import page

class PythonOrgSeach(unittest.TestCase):
    def setUp(self):#works like init
        self.driver=webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://www.python.org")

    # def test_example(self):#anything with keyword test runs upon execution
    
    def test_title(self):
        mainPage=page.MainPage()
        assert mainPage.is_title_matches()


    def tearDown(self):#cleanup
        self.driver.close()

if __name__=="__main__":
    unittest.main
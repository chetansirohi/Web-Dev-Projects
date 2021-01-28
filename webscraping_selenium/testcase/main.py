import unittest #builtin library
from selenium import  webdriver
import page

class PythonOrgSeach(unittest.TestCase):
    def setUp(self):#works like init
        self.driver=webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://www.python.org")

    def test_search_python(self):
        mainPage=page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element ="pycon"
        mainPage.click_go_button()
        search_result_page =page.SearchResultsPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):#cleanup
        self.driver.close()

if __name__=="__main__":
    unittest.main
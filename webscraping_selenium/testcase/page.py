#setup page object
form locator import *

class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

class MainPage(BasePage):
    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element=self.driver.find_element(*MainPageLocators.GO_BUTTON)#unpack
        element.click()

class SearchResultsPage(BasePage):
    def is_results_found(self):# if result found well and good else false
        return "No results found." not in self.driver.page_source


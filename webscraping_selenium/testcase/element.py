from selenium.webdriver.support.ui import WebDriverWait
#for any element for which you want to set values for use this process
class BasePageElement(object):
    def __set__(self,obj,value):
        driver=obj.driver #webdriver
        WebDriverWait(driver,100).until(
            lambda driver:driver.find_element_by_name(self.locator))#equals to the name which we want to find
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self,obj,owner):
        driver=obj.driver #webdriver
        WebDriverWait(driver,100).until(
            lambda driver:driver.find_element_by_name(self.locator))#wait for the element to exist on the page
        element= driver.find_element_by_name(self.locator)
        return element.get_attribute("value") #returns the value we are providing the get method


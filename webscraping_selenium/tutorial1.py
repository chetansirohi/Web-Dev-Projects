

from selenium.webdriver.common.keys import Keys
import time

# path specifies the path of the chrome webdriver used with selenium
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)  # the driver will now run the chrome webdriver
driver.get("https://techwithtim.net")  # by using get we specify the

from selenium import webdriver
# allows us to hit enter,esc,space in search bar
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
# path specifies the path of the chrome webdriver used with selenium
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)  # the driver will now run the chrome webdriver
driver.get("https://techwithtim.net")  # by using get we specify the

link=driver.find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.LINK_TEXT,"Beginner Python Tutorials"))#search for the link text
    ) 
    element.click()#click valid for the button or any link

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))#click element by id -so this is the id of the button that is automatically clicked
    )
    element.click()

    driver.back()#navigate pages backward or forward
    driver.back()
    driver.back()
    driver.forward()
    driver.forward()

except:
    driver.quit()

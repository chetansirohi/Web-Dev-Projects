from selenium import webdriver
# allows us to hit enter,esc,space in search bar
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
import time
#Action Chains and Automating Cookie Clicker

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)  
driver.get("https://orteil.dashnet.org/cookieclicker")  

driver.implicitly_wait(5)#waits the specified time in seconds ,after which the next lines are executed

cookie=driver.find_element_by_id("bigCookie")
cookie_count=driver.find_element_by_id("cookies")
items=[driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]#get the most expensive products first as compared to the least expensive so as to avoid repetitions

actions=ActionChains(driver)#creating instance of actionchain ,actiionchain object will act on the arg->driver
actions.click(cookie)
actions.perform()

for i in range(5000):
    actions.perform()
    count=cookie_count.text.split(" ")[0]
    for item in items:
        value=int(item.text)
        if value <= count:
            upgrade_actions=ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()


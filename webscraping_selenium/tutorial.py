from selenium import webdriver
from selenium.webdriver.common.keys import Keys #allows us to hit enter,esc,space in search bar
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "C:\Program Files (x86)\chromedriver.exe" #path specifies the path of the chrome webdriver used with selenium

#Scripting

driver=webdriver.Chrome(PATH) #the driver will now run the chrome webdriver
driver.get("https://techwithtim.net")#by using get we specify the 
print(driver.title)


#locating Element form Html

search=driver.find_element_by_name("s")#accessing the search bar
search.send_keys("test") #in search bar it will return all the results with keyWord-> test
search.send_keys(Keys.RETURN)
# time.sleep(5) #delays the exit by 5 seconds

try:
    main=WebDriverWait(driver,10).until(#redicted and waited for next page to fetch results
        EC.presence_of_element_located((By.ID,"main"))
    )
    articles=main.find_elements_by_tag_name("article")#the we found all of the elements inside a specific tag
    for article in articles:#lloped through all the titles
        header=article.find_element_by_class_name("entry-summary")#found all the heading -summaries and printed them
        print(header.text)
finally: 
    driver.quit()

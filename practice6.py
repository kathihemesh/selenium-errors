from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://qawikisearch.ccbp.tech/")
inputelement=driver.find_element(By.XPATH,"//input[@id='searchInput']")
inputelement.send_keys("HTML")
searchbtn=driver.find_element(By.XPATH,"//button[@class='search-button']")
searchbtn.click()
driver.implicitly_wait(10)
results=driver.find_element(By.XPATH,"//div[@class='result-item']")

# To count the no of results fetched
time.sleep(20)
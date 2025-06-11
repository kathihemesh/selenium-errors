from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://formy-project.herokuapp.com/")

# page1

#unable to click anchor tag 

AutoComplete=driver.find_element(By.XPATH,"//a[text()='Autocomplete']")
print("element found")
AutoComplete.click()
print("element clicked")

# 

address=driver.find_element(By.ID,"autocomplete")
address.send_keys("Andhra Pradesh,Anantapur district,Tadipatri")
streetaddress=driver.find_element(By.ID,"street_number")
streetaddress.send_keys("krishnapuram 3rd road,Dr.No:-3/511")
streetaddress2=driver.find_element(By.ID,"route")
streetaddress2.send_keys("near putlur road")
locality=driver.find_element(By.ID,"locality")
locality.send_keys("Tadipatri")
state=driver.find_element(By.ID,"administrative_area_level_1")
state.find_element("Andhra Pradesh")
zipcode=driver.find_element(By.ID,"postal_code")
zipcode.find_element("515411")
country=driver.find_element(By.ID,"country")
country.find_element("India")
time.sleep(2)
homebtn=driver.find_element(By.ID,"logo")
homebtn.click()
time.sleep(1)

# page 2

Buttons=driver.find_element(By.XPATH,"//a[text()='Buttons']")
Buttons.click()
time.sleep()
success=driver.find_element(By.XPATH,"//button[text()='Success']")
success.click()
linkbtn=driver.find_element(By.XPATH,"//button[text()='Link']")
linkbtn.click()
middlebtn=driver.find_element(By.XPATH,"//button[text()='Middle']")
middlebtn.click()
btn1=driver.find_element(By.XPATH,"//button[text()='1']")
btn1.click()

time.sleep(10)

# testing branches using checkout


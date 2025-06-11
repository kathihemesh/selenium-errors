from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demoqa.com/automation-practice-form")
firstname=driver.find_element(By.ID,"firstName")
firstname.send_keys("Hemesh Reddy")
lastname=driver.find_element(By.ID,"lastName")
lastname.send_keys("Kathi")
email=driver.find_element(By.ID,"userEmail")
email.send_keys("hemeshreddy77@gmail.com")
gender=driver.find_element(By.CSS_SELECTOR,".custom-control-label")
gender.click()
number=driver.find_element(By.ID,"userNumber")
number.send_keys("7013913849")
dob=driver.find_element(By.ID,"dateOfBirthInput")
dob.send_keys("22 Aug 2006")
time.sleep(2)
subjects=driver.find_element(By.ID,"subjectsInput")
subjects.send_keys("matnshs")
time.sleep(2)
hobbies=driver.find_element(By.CSS_SELECTOR,"label[for='hobbies-checkbox-1']")
hobbies.click()
time.sleep(2)
upload=driver.find_element(By.ID,"uploadPicture")
upload.send_keys("C:\\Users\\hemes\\OneDrive\\Pictures\\Screenshots\\Screenshot 2025-03-25 113221.png")
address=driver.find_element(By.ID,"currentAddress")
address.send_keys("andhra prades,anantapur")

# select dropdowns which isn't a select tag

state=driver.find_element(By.CSS_SELECTOR,"svg[focusable='false']")
state.click()
time.sleep(10)
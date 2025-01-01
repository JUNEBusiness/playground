from seleniumbase import Driver, SB
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# driver.get("https://postman.com")

# WebDriverWait(driver, 2).until(
#     EC.presence_of_element_located((By.ID, "SignIn"))
# )

# signin_button = driver.find_element(By.ID, "SignIn")
# signin_button.click()


# time.sleep(5)

# username_element = driver.find_element(By.ID, "username")
# username_element.clear()
# username_element.send_keys("JUNEBusiness")
# time.sleep(2)
# password_element = driver.find_element(By.ID, "password")
# password_element.clear()
# password_element.send_keys("@Jessie12")
# time.sleep(5)
# verify_element = driver.find_element(By.ID, "cb-lb")
# verify_element.click()
# signin_button = driver.find_element(By.ID, "sign-in-btn")
# signin_button.click()

driver = Driver(uc=True)

url = "https://postman.com"

driver.uc_open_with_reconnect(url,10)


signin_button = driver.find_element(By.ID, "SignIn")
signin_button.click()


time.sleep(5)

username_element = driver.find_element(By.ID, "username")
username_element.clear()
username_element.send_keys("JUNEBusiness")
time.sleep(2)
password_element = driver.find_element(By.ID, "password")
password_element.clear()
password_element.send_keys("@Jessie12")
driver.uc_gui_click_captcha()
signin_button = driver.find_element(By.ID, "sign-in-btn")
signin_button.click()

# driver.execute_script(f'window.verfyRecaptcha("{token}")')
time.sleep(30)

driver.quit()
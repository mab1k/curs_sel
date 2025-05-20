import time

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/")

#login_button = WebDriverWait(driver, 10).until(
#    EC.element_to_be_clickable(("xpath", "//a[@role='button' and text()='Log In']"))
#)
#login_button.click()

email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(("xpath", "//input[@type='email']"))
)
email_field.send_keys("<EMAIL>")

print(email_field.get_attribute("value"))
print(email_field.get_attribute("max length"))
email_field.clear()
time.sleep(5)
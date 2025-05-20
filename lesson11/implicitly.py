import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)

ENABLE_BUTTON = ("xpath", "//button[text()='Enable']")
ENABLE_INPUT = ("xpath", "//input[@type='text']")
driver.get("https://the-internet.herokuapp.com/dynamic_controls")
wait.until(
    EC.element_to_be_clickable(ENABLE_BUTTON)
).click()
wait.until(EC.element_to_be_clickable(ENABLE_INPUT)).send_keys("Hello")
wait.until(EC.text_to_be_present_in_element_value(ENABLE_INPUT, "Hello"))


print("OK")

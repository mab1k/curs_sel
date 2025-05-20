import os
import time

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/upload")

el_file = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(("xpath", "//input[@type='file' and @id='file-upload']"))
)
el_file.send_keys(os.getcwd() + "/downloads/test.txt")
time.sleep(5)

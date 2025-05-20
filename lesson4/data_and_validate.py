import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")
cur_url = driver.current_url
print(cur_url)

cur_title = driver.title
print(cur_title)
print(driver.page_source)
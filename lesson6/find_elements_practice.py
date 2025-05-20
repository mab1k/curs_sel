import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://www.wikipedia.org/")

time.sleep(5)
print(driver.find_elements("class name", "central-featured-lang.lang2")[0].click())
time.sleep(5)
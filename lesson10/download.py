import os
import time

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": r"C:\Users\ppiv0\PycharmProjects\test_selenium\lesson10\downloads",
    "download.prompt_for_download": False,  # Отключаем диалог подтверждения
}
chrome_options.add_experimental_option("prefs", prefs)


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/download")

files_to_download = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(("xpath", "//a"))
)
print(files_to_download[3].click())
time.sleep(10)
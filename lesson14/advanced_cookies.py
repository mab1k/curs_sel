import os
import time

import pickle
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--window-size=1920x1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/ru/ru/login")
'''
INPUT_FIELD_LOGIN = "//input[@aria-label='Введите адрес электронной почты' and @id='login_email']"
INPUT_FIELD_PASSWORD = "//input[@aria-label='Введите пароль' and @id='password']"
BUTTON_LOGIN = "//button[@id='loginformsubmit']"


input_field_login = wait.until(EC.visibility_of_element_located(("xpath", INPUT_FIELD_LOGIN))).send_keys("piv0004@yandex.ru")
input_field_password = wait.until(EC.visibility_of_element_located(("xpath", INPUT_FIELD_PASSWORD))).send_keys("Cvtifhbrb228")
wait.until(EC.element_to_be_clickable(("xpath", BUTTON_LOGIN))).click()

# Создаем папку для кук, если она не существует
cookies_dir = os.path.join(os.getcwd(), "cookies")
os.makedirs(cookies_dir, exist_ok=True)

# Сохраняем куки в файл
cookie_path = os.path.join(cookies_dir, "cookies.pkl")
pickle.dump(driver.get_cookies(), open(cookie_path, "wb"))

time.sleep(5)
'''
cookies_dir = os.path.join(os.getcwd(), "cookies")
cookie_path = os.path.join(cookies_dir, "cookies.pkl")
driver.delete_all_cookies()
cookies = pickle.load(open(cookie_path, "rb"))


for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(5)
driver.refresh()
time.sleep(5)
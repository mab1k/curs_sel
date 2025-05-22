import time


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--window-size=1920x1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)


driver.get("https://demoqa.com/alerts")
driver.save_screenshot('screenshot.png')

BUTTON_1 = ("xpath", "//button[@id='alertButton']")
BUTTON_3 = ("xpath", "//button[@id='confirmButton']")
BUTTON_4 = ("xpath", "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(BUTTON_4)).click()

alert = wait.until(EC.alert_is_present())

driver.switch_to.alert

time.sleep(3)
alert.send_keys("Hello")
time.sleep(3)
alert.accept()
time.sleep(3)

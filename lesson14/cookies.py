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
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/ru/ru/login")

#print(driver.get_cookie("country_code"))
print(driver.get_cookies()
      )
driver.add_cookie({
      "name": "Example",
      "value": "Kukushka"
})

print(driver.get_cookie("Example"))

before = driver.get_cookie("split")
print(before)

driver.delete_cookie("split")

driver.add_cookie({
      "name": "split",
      "value": "QWERY"
})

after = driver.get_cookie("split")
print(after)

driver.delete_all_cookies()

driver.add_cookie({
      "name": "split",
      "value": "QWERY"
})
print(driver.get_cookies())


time.sleep(20)
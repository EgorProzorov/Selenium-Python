from selenium import webdriver
import time
import random
from fake_useragent import UserAgent
user_agent_list = [
    "gondon1",
    "pidoras300",
    "smallpenis1"
]
useragent = UserAgent()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"

options = webdriver.FirefoxOptions()

options.set_preference("general.useragent.override", "Hello gon123!")

driver = webdriver.Firefox(
    executable_path="/Users/egorprozorov/PycharmProjects/PrarsingTest/geckodriver",
    options=options)

try:
    driver.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
    #driver.save_screenshot("1.png")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
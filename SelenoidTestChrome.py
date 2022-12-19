from selenium import webdriver
import time
import random
from fake_useragent import UserAgent
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
user_agent_list = [
    "gondon1",
    "pidoras300",
    "smallpenis1"
]
useragent = UserAgent()
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={random.choice(user_agent_list)}")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
try:
    driver.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
    #driver.save_screenshot("1.png")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

data =[]
url = "https://rodion-de-front.github.io/RECIPES-ONLINE/"

options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(
    executable_path="/Users/egorprozorov/PycharmProjects/PrarsingTest/geckodriver",
    options=options
)

try:
    driver.get(url=url)
    button_input = driver.find_element(By.XPATH, "//div[3]/div[2]/div[2]/input[3]")
    button_input.click()
    time.sleep(5)
    printed_info = driver.find_element(By.ID, "cards")
    answer = printed_info.text.split('\n')
    closer = driver.find_element(By.CLASS_NAME, "closeModal")
    for i in range(len(answer)):
        driver.find_element(By.XPATH, f"//div[{i+1}]/img").screenshot(f'{i+1}img.png')

except Exception as ex:
    print(ex)

finally:
    driver.close()


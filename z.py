from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service("./chromedriver.exe"))
txt = "My name is sunil"
driver.get("https://tapshare.xyz/")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, '.btn-add-code').click()
time.sleep(5)

a = driver.find_element(By.CSS_SELECTOR, 'input[name="title"]')
textarea = driver.find_element(By.CSS_SELECTOR, 'textarea')
driver.execute_script("""
    arguments[0].value = arguments[1];
    arguments[2].value = arguments[3];
""", a, "Sunil", textarea, txt)

driver.find_element(By.CSS_SELECTOR, "button[role='submit']").click()
time.sleep(6)
code = driver.find_element(By.CSS_SELECTOR, '#root > div > div > div:nth-child(3) > div.px-3.py-2 > div > button')
code.click()
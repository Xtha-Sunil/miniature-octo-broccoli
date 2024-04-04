from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import pyperclip
import time

class LeetcodeAutomation:
    def __init__(self, profile_path, executable_path):
        self.profile_path = profile_path
        self.executable_path = executable_path
        self.driver = self._create_driver()

    def _create_driver(self):
        options = Options()
        options.add_argument(f"--user-data-dir={self.profile_path}")
        return webdriver.Chrome(service=Service(executable_path=self.executable_path), options=options)

    def wait_for_element(self, by, value):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((by, value)))

    def get_code(self, new_code):
        if new_code != "":
            return new_code

        date=datetime.now().strftime('%Y_%m_%d')
        self.driver.get(f"https://github.com/Sunil-Shrestha07/LeetcodeSolution/blob/main/{date}.cpp")
        self.wait_for_element(By.CSS_SELECTOR, 'button[aria-label="Copy raw content"]').click()
        time.sleep(2)  # Wait for copying to be done
        return pyperclip.paste()

    def goto_potd(self):
        self.driver.execute_script("window.open('https://www.leetcode.com/problemset', '_blank')")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_for_element(By.CSS_SELECTOR, ".truncate a").click()
        self.wait_for_element(By.CSS_SELECTOR, ".ant-select-arrow").click()
        self.wait_for_element(By.CSS_SELECTOR, "li[data-cy='lang-select-C++']").click()

    def set_and_submit_code(self, new_code):    
        codemirror_div = self.driver.find_element(By.CLASS_NAME, "CodeMirror")
        self.driver.execute_script("arguments[0].CodeMirror.setValue(arguments[1]);", codemirror_div, new_code)
        self.wait_for_element(By.CLASS_NAME, "submit__2ISl").click()
        time.sleep(5)

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    BASE_PATH = "C:/Users/User/AppData/Local/Google/Chrome/User Data/"
    EXECUTABLE_PATH = "chromedriver.exe"

    profiles = ["LeetcodeAutomation", "id1"]
    new_code = ""

    for profile in profiles:
        automation = LeetcodeAutomation(BASE_PATH+profile, EXECUTABLE_PATH)
        new_code = automation.get_code(new_code)
        automation.goto_potd()
        automation.set_and_submit_code(new_code)
        time.sleep(5)
        automation.close()
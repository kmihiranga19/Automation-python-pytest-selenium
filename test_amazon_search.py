import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)
driver.maximize_window()
driver.get("https://www.aliexpress.com/")


def remove_popups_message():
    try:
        pop_close_btn = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "pop-close-btn")))
        pop_close_btn.click()

    except NoSuchElementException:
        pass

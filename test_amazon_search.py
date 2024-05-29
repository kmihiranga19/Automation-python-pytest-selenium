import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configuration

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)
driver.maximize_window()
driver.get(configuration.BaseURL)


def remove_popups_message():
    try:
        pop_close_btn = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "pop-close-btn")))
        pop_close_btn.click()

    except NoSuchElementException:
        pass

    def remove_popup_notification():
        try:
            do_not_do_allow = driver.find_element(By.CSS_SELECTOR, 'img[src="https://img.alicdn.com/tfs/TB1GSux3fb2gK0jSZK9XXaEgFXa-21-21.png"]')
            do_not_do_allow.click()

        except NoSuchElementException:
            print("No")

    remove_popup_notification()


remove_popups_message()

# @author : @geeksforgeeks

import time
from selenium.webdriver.common.by import By


def scroll_to_bottom(driver):
    last_height = driver.execute_script('return document.body.scrollHeight')

    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

        # waiting for the results to load
        # Increase the sleep time if your internet is slow
        time.sleep(3)

        new_height = driver.execute_script('return document.body.scrollHeight')

        # click on "Show more results" (if exists)
        try:
            driver.find_element(By.CLASS_NAME, "mye4qd").click()

            # waiting for the results to load
            # Increase the sleep time if your internet is slow
            time.sleep(3)
        except:
            pass

        # checking if we have reached the bottom of the page
        if new_height == last_height:
            break

        last_height = new_height

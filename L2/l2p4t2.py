import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()

try:
    browser.get(link)
    check_price = WebDriverWait(browser, 8).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button = browser.find_element_by_id("book").click()
    x_param = browser.find_element_by_id("input_value").text
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(str(math.log(abs(12*math.sin(int(x_param))))))
    submit_button = browser.find_element_by_id("solve").click()

finally:
    time.sleep(10)
    browser.quit()

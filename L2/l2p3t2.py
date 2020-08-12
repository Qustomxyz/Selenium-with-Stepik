import math
import time
from selenium import webdriver


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    button = browser.find_element_by_tag_name('button').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    number = browser.find_element_by_id("input_value").text
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(str(math.log(abs(12 * math.sin(int(number))))))
    submit_button = browser.find_element_by_class_name("btn-primary")
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()

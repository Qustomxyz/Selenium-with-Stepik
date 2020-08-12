import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    x_param = browser.find_element_by_id("input_value")
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(calc(x_param.text))

    checkbox_button = browser.find_element_by_id("robotCheckbox")
    checkbox_button.click()

    radio_button = browser.find_element_by_id("robotsRule")
    radio_button.click()

    submit_button = browser.find_element_by_class_name("btn-default")
    submit_button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

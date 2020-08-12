import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(x, y):
    return str(int(x) + int(y))


link = "http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    num_1 = browser.find_element_by_id("num1").text
    num_2 = browser.find_element_by_id("num2").text
    index = calc(num_1, num_2)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(index)

    submit_button = browser.find_element_by_class_name("btn-default").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

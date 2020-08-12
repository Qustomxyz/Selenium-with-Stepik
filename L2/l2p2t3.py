import os
import time
from selenium import webdriver

my_dir = os.path.abspath(os.path.dirname(__file__))
my_file = os.path.join(my_dir, 'test.txt')

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    elements = browser.find_elements_by_xpath('//input[@type="text"]')
    for element in elements:
        element.send_keys('Тестовый текст')

    file_element = browser.find_element_by_xpath('//input[@type="file"]')
    file_element.send_keys(my_file)
    button_submit = browser.find_element_by_xpath('//button[@type="submit"]').click()
finally:
    time.sleep(10)
    browser.quit()

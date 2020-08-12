import time
from selenium import webdriver

link = "https://qustomxyz.github.io/check-selenium/"

browser = webdriver.Chrome()

try:
    browser.get(link)
    element = browser.find_element_by_id("id")
    true_element = element.get_attribute("true")
    checked = element.get_attribute("checked")
    print(f'try find true: {true_element} as type {type(true_element)}')
    print(f'try find checked: {checked} as type {type(checked)}')
finally:
    time.sleep(10)
    browser.quit()
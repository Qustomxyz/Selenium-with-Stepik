from selenium import webdriver
import time

try:
	link = "http://suninjuly.github.io/registration2.html"
	browser = webdriver.Chrome()
	browser.get(link)

	# Ваш код, который заполняет обязательные поля
	firstNameInput = browser.find_element_by_css_selector("div.first_block div.first_class input.first")
	firstNameInput.send_keys("Ivan")
	lastNameInput = browser.find_element_by_css_selector("div.first_block div.second_class input.second")
	lastNameInput.send_keys("Petrov")
	emailInput = browser.find_element_by_css_selector("div.first_block div.third_class input.third")
	emailInput.send_keys("ivan@petrov.ya")
	
	# Отправляем заполненную форму

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

	time.sleep(1)

	welcome_text_elt = browser.find_element_by_css_selector("h1")

	welcome_text = welcome_text_elt.text

	assert "Congratulations! You have successfully registered!" == welcome_text

finally:
	time.sleep(10)
	browser.quit()

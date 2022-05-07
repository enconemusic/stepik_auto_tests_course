from selenium import webdriver
import time
import math
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'text.txt')

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    name=browser.find_element_by_name("firstname")
    name.send_keys("aleksey")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("aleksandrov")
    email = browser.find_element_by_name("email")
    email.send_keys("aleksandrov@r.com")
    file = browser.find_element_by_name("file")
    file.send_keys(file_path)
    button = browser.find_element_by_css_selector(".btn.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
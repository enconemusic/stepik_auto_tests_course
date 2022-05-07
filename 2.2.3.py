from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select



try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    sum = int(x) + int(y)
    dd = Select(browser.find_element_by_id("dropdown"))
    dd.select_by_value(str(int(x) + int(y)))
    button = browser.find_element_by_css_selector(".btn.btn")
    button.click()
finally:
    time.sleep(1)
    browser.quit()
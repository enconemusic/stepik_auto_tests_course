from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_elem = browser.find_element_by_id("input_value")
    x = x_elem.text
    y=calc(x)
    inp=browser.find_element_by_id("answer")
    inp.send_keys(y)
    chck1 = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", chck1)
    chck1.click()
    rb1=browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rb1)
    rb1.click()


    button = browser.find_element_by_css_selector(".btn.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
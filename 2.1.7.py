from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)
    chck1 = browser.find_element_by_id("robotCheckbox")
    chck1.click()
    rb1=browser.find_element_by_id("robotsRule")
    rb1.click()
    inp=browser.find_element_by_id("answer")
    inp.send_keys(y)
    button = browser.find_element_by_css_selector(".btn.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
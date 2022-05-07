from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element_by_css_selector(".trollface")
    btn.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    value = browser.find_element_by_id("input_value")
    x = value.text
    y = calc(x)
    inp = browser.find_element_by_id("answer")
    inp.send_keys(y)
    button = browser.find_element_by_css_selector(".btn.btn")
    button.click()
finally:
    time.sleep(20)
    browser.quit()
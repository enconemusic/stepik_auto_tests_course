from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
values = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element_by_id("book")
button.click()
value = browser.find_element_by_id("input_value")
x = value.text
y = calc(x)
inp = browser.find_element_by_id("answer")
inp.send_keys(y)
submit = browser.find_element_by_id("solve")
submit.click()
time.sleep(20)
browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
url = "http://suninjuly.github.io/math.html"
browser.get(url)

try:
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    line = browser.find_element_by_id("answer")
    line.send_keys(str(y))
        
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    submit = browser.find_element_by_class_name("btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

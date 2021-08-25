from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def main():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    browser.find_element_by_class_name("btn").click()

    redirect_page_name = browser.window_handles[1]
    browser.switch_to.window(redirect_page_name)

    calc_value = calc(int(browser.find_element_by_id("input_value").text))
    browser.find_element_by_id("answer").send_keys(str(calc_value))
    
    browser.find_element_by_class_name("btn").click()

    code_value = browser.switch_to.alert()
    print(code_value.text)

try:
    main()
finally:
    browser.quit()

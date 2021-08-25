from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()


def main():
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element_by_class_name("btn").click()
    alert_confirm = browser.switch_to.alert
    alert_confirm.accept()
    check_value = calc(int(browser.find_element_by_id("input_value").text))
    browser.find_element_by_id("answer").send_keys(str(check_value))
    browser.find_element_by_class_name("btn").click()    

    alert_code = browser.switch_to.alert.text
    browser.switch_to.alert.accept()
    print(alert_code)

    
try:
    main()


finally:
    browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

 
browser = webdriver.Chrome()
url = "http://suninjuly.github.io/get_attribute.html"


try:
    browser.get(url)

    chest = browser.find_element_by_id("treasure")
    xvalue = chest.get_attribute("valuex")
    value = calc(xvalue)
    
    textline = browser.find_element_by_id("answer")
    textline.send_keys(str(value))

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    submit = browser.find_element_by_class_name("btn")
    submit.click()
    
finally:
    time.sleep(10)
    webdriver.quit()

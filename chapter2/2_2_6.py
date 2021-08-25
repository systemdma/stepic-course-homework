from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    

browser = webdriver.Chrome()


try:
    browser.get("http://suninjuly.github.io/execute_script.html")

    x_value = browser.find_element_by_id("input_value")
    x_calculated = calc(int(x_value.text))
    
    browser.execute_script('textline=document.getElementById("answer");textline.scrollIntoView();')
    browser.find_element_by_id("answer").send_keys(str(x_calculated))

    browser.execute_script('checkbox=document.getElementById("robotCheckbox");checkbox.scrollIntoView();')
    browser.find_element_by_id("robotCheckbox").click()

    browser.execute_script('radio=document.getElementById("robotsRule");radio.scrollIntoView()')
    browser.find_element_by_id("robotsRule").click()

    browser.execute_script('butt = document.getElementsByClassName("btn")[0];butt.scrollIntoView()')
    browser.find_element_by_class_name("btn").click()
    
finally:
    time.sleep(10)
    browser.quit()

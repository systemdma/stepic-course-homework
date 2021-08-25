from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


url = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(url)

    calc_result = str(int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text))
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(calc_result)

    browser.find_element_by_class_name("btn").click()

    
finally:
    time.sleep(10)
    browser.quit()

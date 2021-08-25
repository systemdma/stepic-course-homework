from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


browser = webdriver.Chrome()


def main():
    #open page
    browser.get("http://suninjuly.github.io/file_input.html")

    #ender data to textlines
    browser.find_element_by_css_selector('input[name="firstname"]').send_keys("Ivan")
    browser.find_element_by_css_selector('input[name="lastname"]').send_keys("Ivanov")
    browser.find_element_by_css_selector('input[name="email"]').send_keys("Ivan@ya.ru")
        
    #create empty file    
    file = open(os.path.dirname(__file__) + "/file.txt", "w+")
    file.close()
    #send file
    directory = os.path.abspath(__file__).replace("2_2_8.py", "file.txt")
    browser.find_element_by_id("file").send_keys(directory)

    #click on submit button
    browser.find_element_by_class_name("btn").click()


try:
    main()


finally:
    browser.quit()

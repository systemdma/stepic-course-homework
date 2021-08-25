from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def main():
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    browser.find_element_by_id("book").click()
    
    browser.execute_script('btn=document.getElementById("solve");btn.scrollIntoView();')
    browser.find_element_by_id("answer").send_keys(str(calc(int(browser.find_element_by_id("input_value").text))))
    browser.find_element_by_id("solve").click()

    alert_with_code = browser.switch_to.alert
    print(alert_with_code.text)

try:
    main()


finally:
    time.sleep(10)
    browser.quit()

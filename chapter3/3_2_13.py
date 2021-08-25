from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 


class registration_required_url1_test(unittest.TestCase):

    def test_register_url1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
    
        #send data
        browser.find_element_by_xpath('//input[contains(@placeholder, "first name")]').send_keys("Ivan")
        browser.find_element_by_xpath('//input[contains(@placeholder, "last name")]').send_keys("Ivanov")
        browser.find_element_by_xpath('//input[contains(@placeholder, "email")]').send_keys("Email")
        browser.find_element_by_class_name("btn").click()
    
        #wait new page
        wait = WebDriverWait(browser, 2)
        wait.until(expected_conditions.title_is("Welcome!"))
    
        #assert register status
        result_text = browser.find_element_by_tag_name("h1").text
        self .assertEqual(result_text, "Congratulations! You have successfully registered!")
            
        browser.quit()

    def test_register_url2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
    
        #send data
        browser.find_element_by_xpath('//input[contains(@placeholder, "first name")]').send_keys("Ivan")
        browser.find_element_by_xpath('//input[contains(@placeholder, "last name")]').send_keys("Ivanov")
        browser.find_element_by_xpath('//input[contains(@placeholder, "email")]').send_keys("Email")
        browser.find_element_by_class_name("btn").click()
    
        #wait new page
        wait = WebDriverWait(browser, 2)
        wait.until(expected_conditions.title_is("Welcome!"))
    
        #assert register status
        result_text = browser.find_element_by_tag_name("h1").text
        self .assertEqual(result_text, "Congratulations! You have successfully registered!")
            
        browser.quit()


if __name__ == "__main__":
    unittest.main()

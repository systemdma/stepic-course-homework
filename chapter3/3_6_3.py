from selenium import webdriver
import time
import math
import pytest
from selenium.webdriver.common.by import By


urls = ["https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"]


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize('url', urls)
def test_stepic_tasks(driver, url):
    driver.get(url)
    driver.implicitly_wait(10)
    answer = str(math.log(int(time.time())))
    driver.find_element_by_class_name("textarea").send_keys(answer)
    driver.find_element_by_class_name("submit-submission").click()
    assert driver.find_element_by_class_name("smart-hints__hint").text == "Correct!", "Not right reply on answer"
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_should_has_add_button_to_cart(browser):
    browser.get(link)

    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"))
    )

    button_is_exist = \
        browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']").is_displayed()


    assert button_is_exist == True








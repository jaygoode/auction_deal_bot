from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


class Selenium_functions:
    def __init__(self) -> None:
        self.website_address = "http://www.huutokaupat.com"
        self.driver = webdriver.Chrome()
        self.driver.get(self.website_address)


def login_to_huutokaupat(self):
    cookies_warning_popup_xpath = "//div/button[text()='Vain välttämättömät']"
    sleep(5)
    if is_element(self.driver, cookies_warning_popup_xpath):
        self.driver.find_element(
            By.XPATH, "//div/button[text()='Vain välttämättömät']"
        ).click()
    sleep(5)
    login_nav_button = self.driver.find_element(By.XPATH, "//div/nav/ul/li[4]").click()

    username = input("username: ")
    pwd = input("pwd: ")

    email_input = self.driver.find_element(
        By.XPATH, "//div/input[@type = 'email']"
    ).send_keys(username)
    pwd_input = self.driver.find_element(
        By.XPATH, "//div/input[@type = 'password']"
    ).send_keys(pwd)

    login_btn = self.driver.find_element(
        By.XPATH, "//button[text()='Kirjaudu']"
    ).click()

    sleep(5)
    oma_sivu_xpath = "//span[text()='Oma sivu']"
    if is_element(self.driver, cookies_warning_popup_xpath):
        print("Login successful!")
    else:
        print("Login failed..")

    breakpoint()


def search_items(self):
    pass


def add_to_following_list(self):
    pass


def is_element(self, xpath):
    elements = self.driver.find_elements(By.XPATH, xpath)
    return len(elements) > 0

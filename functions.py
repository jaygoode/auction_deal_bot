from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def open_huutokaupat():
    website_address = "http://www.huutokaupat.com"
    driver = webdriver.Chrome()
    driver.get(website_address)
    return driver


def login_to_huutokaupat(driver):
    cookies_warning_popup_xpath = "//div/button[text()='Vain välttämättömät']"
    sleep(5)
    if is_element(driver, cookies_warning_popup_xpath):
        driver.find_element(
            By.XPATH, "//div/button[text()='Vain välttämättömät']"
        ).click()
    sleep(5)
    login_nav_button = driver.find_element(By.XPATH, "//div/nav/ul/li[4]").click()
    username = input("username: ")
    pwd = input("pwd: ")
    email_input = driver.find_element(
        By.XPATH, "//div/input[@type = 'email']"
    ).send_keys(username)
    pwd_input = driver.find_element(
        By.XPATH, "//div/input[@type = 'password']"
    ).send_keys(pwd)

    login_btn = driver.find_element(By.XPATH, "//button[text()='Kirjaudu']").click()

    oma_sivu_xpath = "//span[text()='Oma sivu']"
    if is_element(driver, cookies_warning_popup_xpath):
        print("Login successful!")
    else:
        print("Login failed..")

    breakpoint()


def search_items(driver):
    pass


def add_to_following_list(driver):
    pass


def is_element(driver, xpath):
    elements = driver.find_elements(By.XPATH, xpath)
    return len(elements) > 0

from selenium import webdriver
from selenium.webdriver.common.by import By


def open_huutokaupat():
    chromedriver_path = ""
    website_address = "www.huutokaupat.fi"
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.get(website_address)
    return driver


def login_to_huutokaupat(driver):
    login_nav_button = driver.find_element(By.XPATH, "//div/nav/ul/li[4]")
    pass


def search_items(driver):
    pass


def add_to_following_list(driver):
    pass

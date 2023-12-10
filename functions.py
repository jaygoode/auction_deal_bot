import smtplib
from email.message import EmailMessage
import getpass
import re
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
        sleep(2)
        if self.is_element(cookies_warning_popup_xpath):
            self.driver.find_element(
                By.XPATH, "//div/button[text()='Vain välttämättömät']"
            ).click()
        sleep(1)
        # login_nav_button = self.driver.find_element(
        #     By.XPATH, "//div/nav/ul/li[4]"
        # ).click()

        # username = input("username: ")

        # password = getpass.getpass(prompt="Password: ")

        # email_input = self.driver.find_element(
        #     By.XPATH, "//div/input[@type = 'email']"
        # ).send_keys(username)
        # pwd_input = self.driver.find_element(
        #     By.XPATH, "//div/input[@type = 'password']"
        # ).send_keys(password)

        # login_btn = self.driver.find_element(
        #     By.XPATH, "//button[text()='Kirjaudu']"
        # ).click()

        # sleep(5)
        # oma_sivu_xpath = "//span[text()='Oma sivu']"
        # if self.is_element(cookies_warning_popup_xpath):
        #     print("Login successful!")
        # else:
        #     print("Login failed..")

    def search_items(self):
        search_btn = self.driver.find_element(
            By.XPATH, "//button[@aria-label='Näytä haku']"
        )
        search_btn.click()

        search_input = self.driver.find_element(By.XPATH, "//input[@type='search']")
        # search_item = input("Search: ")
        search_item = "moottoripyörä"
        search_input.send_keys(search_item)

        search_btn_submit = self.driver.find_element(
            By.XPATH, "//button[@type='submit']"
        )
        search_btn_submit.click()

    def find_items_within_range(self):
        # input_max_price = int(input("Add max price(€): "))
        # input_max_time_left = int(input("Add max time left days: "))
        input_max_price = 10000
        input_max_time_left = 100
        sleep(3)
        all_postings_on_page = self.driver.find_elements(
            By.XPATH, "//div[@class='list-entry visible']"
        )
        found_postings = []

        for post in all_postings_on_page:
            highest_bid, time_left = self._get_bids_and_time_left(post)

            if not highest_bid:
                continue

            if highest_bid < input_max_price and time_left < input_max_time_left:
                anchor_tag = post.find_element(By.XPATH, ".//a")
                post_link = anchor_tag.get_attribute("href")
                found_postings.append(post_link)

        print(found_postings)
        return found_postings

    def send_mail(self, postings):
        msg = EmailMessage()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.set_content(body)

        try:
            server = smtplib.SMTP("smtp.office365.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            server.quit()

        sender_email = "your_email@example.com"
        receiver_email = "recipient@example.com"
        subject = "Test Email via Python"
        body = "This is a test email sent via Python."

        sender_password = "your_password"

    def is_element(self, xpath):
        elements = self.driver.find_elements(By.XPATH, xpath)
        return len(elements) > 0

    def _get_bids_and_time_left(self, post):
        highest_bid = post.find_element(
            By.XPATH, "//span[@class='entry-highest-bid']"
        ).text
        time_left_days = post.find_element(
            By.XPATH, "//span[@class='timeleft-short']"
        ).text
        highest_bid_clean = re.sub(r"\D", "", highest_bid)
        time_left_clean = re.sub(r"\D", "", time_left_days)
        try:
            highest_bid_int = int(highest_bid_clean)
        except:
            print("could not convert bid to int. skipping..")
            return False, None

        try:
            time_left_clean_int = int(time_left_clean)
        except:
            print(
                "could not convert days to int. might be less than one day. setting days left to 0."
            )
            time_left_clean_int = 0
        return highest_bid_int, time_left_clean_int

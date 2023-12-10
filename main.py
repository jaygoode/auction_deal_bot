from functions import (
    Selenium_functions,
)


def main():
    selenium = Selenium_functions()
    selenium.login_to_huutokaupat()
    selenium.search_items()
    postings = selenium.find_items_within_range()
    selenium.send_mail(postings)


if __name__ == "__main__":
    main()

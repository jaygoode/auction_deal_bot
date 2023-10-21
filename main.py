from functions import (
    open_huutokaupat,
    login_to_huutokaupat,
    search_items,
    add_to_following_list,
)


def main():
    driver = open_huutokaupat()
    login_to_huutokaupat(driver)
    search_items(driver)
    add_to_following_list(driver)


if __name__ == "__main__":
    main()

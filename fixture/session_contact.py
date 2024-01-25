from selenium.webdriver.common.by import By


class SessionHelperContact:

    def __init__(self, app_contact):
        self.app_contact = app_contact

    def login(self, username, password):
        wd = self.app_contact.driver

        self.app_contact.go_to_home_page()
        wd.get("http://localhost/addressbook/")
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):
        self.app_contact.driver.find_element(By.LINK_TEXT, "Logout").click()
from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.driver
        self.app.open_home_page()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").send_keys(password)

    def logout(self):
        self.app.driver.find_element(By.LINK_TEXT, "Logout").click()

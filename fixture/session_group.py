from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.app.open_home_page()
        self.app.driver.find_element(By.NAME, "user").click()
        self.app.driver.find_element(By.NAME, "user").send_keys(username)
        self.app.driver.find_element(By.NAME, "pass").click()
        self.app.driver.find_element(By.NAME, "pass").send_keys(password)

    def logout(self):
        self.app.driver.find_element(By.LINK_TEXT, "Logout").click()

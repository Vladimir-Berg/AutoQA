from selenium import webdriver
from fixture.session_group import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1070, 759)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.driver
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        wd = self.driver
        wd.quit()

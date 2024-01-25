from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session_group import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1070, 759)
        self.session = SessionHelper(self)

    def return_to_groups(self):
        wd = self.driver
        wd.find_element(By.LINK_TEXT, "group page").click()

    def create_new_group(self, group):
        wd = self.driver
        self.open_groups_page()
        # create new group
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups()

    def open_groups_page(self):
        wd = self.driver
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
        wd.find_element(By.LINK_TEXT, "groups").click()

    def open_home_page(self):
        wd = self.driver
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        wd = self.driver
        wd.quit()

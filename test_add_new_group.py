import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from group import Group
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestLoginAddGroup():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_add_group(self):
        self.open_home_page()
        self.set_window_size()
        self.login("admin", "secret")
        self.open_groups_page()
        self.create_new_group(Group("Group", "Header", "Comment"))
        self.return_to_groups()
        self.logout()
        self.driver.close()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups(self):
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def create_new_group(self, group):
        # create new group
        self.driver.find_element(By.NAME, "new").click()
        # fill group form
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit
        self.driver.find_element(By.NAME, "submit").click()

    def open_groups_page(self):
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").click()
        self.driver.find_element(By.NAME, "pass").send_keys(password)

    def set_window_size(self):
        self.driver.set_window_size(1070, 759)

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

import time

from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_homepage(self):
        self.app.driver.find_element(By.LINK_TEXT, "home page").click()

    def create(self, contact):
        wd = self.app.driver
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        wd.find_element(By.NAME, "bday").click()
        dropdown = wd.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, contact.bday).click()
        wd.find_element(By.NAME, "bmonth").click()
        dropdown = wd.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, contact.bmonth).click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        wd.find_element(By.NAME, "new_group").click()
        dropdown = wd.find_element(By.NAME, "new_group")
        dropdown.find_element(By.XPATH, contact.new_group).click()
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(75)").click()
        self.return_to_homepage()

    def edit(self, contact):
        wd = self.app.driver
        time.sleep(2)
        wd.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > .center:nth-child(8) img").click()
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        wd.find_element(By.NAME, "bday").click()
        dropdown = wd.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, contact.bday).click()
        wd.find_element(By.NAME, "bmonth").click()
        dropdown = wd.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, contact.bmonth).click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(74)").click()
from selenium import webdriver
from selenium.webdriver.common.by import By


class ApplicationContact:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1070, 760)

    def destroy(self):
        self.driver.quit()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_homepage(self):
        self.driver.find_element(By.LINK_TEXT, "home page").click()

    def creeate_contact(self, contact):
        self.driver.find_element(By.LINK_TEXT, "add new").click()
        self.driver.find_element(By.NAME, "firstname").click()
        self.driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.driver.find_element(By.NAME, "middlename").click()
        self.driver.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        self.driver.find_element(By.NAME, "lastname").click()
        self.driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.driver.find_element(By.NAME, "nickname").click()
        self.driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        self.driver.find_element(By.NAME, "company").click()
        self.driver.find_element(By.NAME, "company").send_keys(contact.company)
        self.driver.find_element(By.NAME, "address").click()
        self.driver.find_element(By.NAME, "address").send_keys(contact.address)
        self.driver.find_element(By.NAME, "mobile").click()
        self.driver.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys(contact.email)
        self.driver.find_element(By.NAME, "bday").click()
        dropdown = self.driver.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, contact.bday).click()
        self.driver.find_element(By.NAME, "bmonth").click()
        dropdown = self.driver.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, contact.bmonth).click()
        self.driver.find_element(By.NAME, "byear").click()
        self.driver.find_element(By.NAME, "byear").send_keys(contact.byear)
        self.driver.find_element(By.NAME, "new_group").click()
        dropdown = self.driver.find_element(By.NAME, "new_group")
        dropdown.find_element(By.XPATH, contact.new_group).click()
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(75)").click()
        self.return_to_homepage()

    def login(self, username, password):
        self.go_to_home_page()
        self.driver.get("http://localhost/addressbook/")
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").click()
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def go_to_home_page(self):
        self.driver.get("http://localhost/addressbook/")

import time
from selenium.webdriver.common.by import By
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.driver
        if not (wd.find_element(By.XPATH, "//*[@id='search-az']/form/input") is True):
            wd.find_element(By.LINK_TEXT, "home").click()

    def return_to_homepage(self):
        self.app.driver.find_element(By.LINK_TEXT, "home page").click()

    def count(self):
        wd = self.app.driver
        self.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def edit(self, contact):
        wd = self.app.driver
        time.sleep(2)
        self.open_home_page()
        wd.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > .center:nth-child(8) img").click()
        self.fill_form(contact)
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(74)").click()
        self.return_to_homepage()

    def create(self, contact):
        wd = self.app.driver
        self.open_home_page()
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_form(contact)
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(75)").click()
        self.return_to_homepage()

    def fill_form(self, contact):
        wd = self.app.driver
        self.change_form_text("firstname", contact.firstname)
        self.change_form_text("middlename", contact.middlename)
        self.change_form_text("lastname", contact.lastname)
        self.change_form_text("nickname", contact.nickname)
        self.change_form_text("company", contact.company)
        self.change_form_text("address", contact.address)
        self.change_form_text("mobile", contact.mobile)
        self.change_form_text("email", contact.email)
        self.change_form_select("bday", contact.bday)
        self.change_form_select("bmonth", contact.bmonth)
        self.change_form_text("byear", contact.byear)

    def change_form_select(self, field_name, select):
        wd = self.app.driver
        if select is not None:
            wd.find_element(By.NAME, field_name).click()
            dropdown = wd.find_element(By.NAME, field_name)
            select = "//option[. = '" + select + "']"
            dropdown.find_element(By.XPATH, select).click()

    def change_form_text(self, field_name, text):
        wd = self.app.driver
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def delete(self):
        wd = self.app.driver
        wd.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > .center:nth-child(8) img").click()
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()

    def get_contacts_list(self):
        wd = self.app.driver
        self.open_home_page()
        contacts = []
        el_index = 2            # запись начинается со второй строки в таблице
        for element in wd.find_elements(By.NAME, "entry"):
            text_first = element.find_element(By.XPATH, ("//*[@id='maintable']/tbody/tr[" + str(el_index) + "]/td[3]")).text
            text_last = element.find_element(By.XPATH, ("//*[@id='maintable']/tbody/tr[" + str(el_index) + "]/td[2]")).text
            contact_id = element.find_element(By.NAME, "selected[]").get_attribute("value")
            contacts.append(Contact(firstname=text_first, lastname=text_last, id=contact_id))
            el_index += 1
            print(contacts[-1])
        return contacts

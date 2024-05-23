import time
from selenium.webdriver.common.by import By
from model.contact import Contact
import re
from selenium.common.exceptions import NoSuchElementException


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.driver
        try:
            found = wd.find_element(By.XPATH, "//*[@id='search-az']/form/input")
        except NoSuchElementException:
            wd.find_element(By.CSS_SELECTOR, "#nav > ul > li:nth-child(1) > a").click()

    def return_to_homepage(self):
        self.app.driver.find_element(By.LINK_TEXT, "home page").click()

    def count(self):
        wd = self.app.driver
        self.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def fill_form(self, contact):
        self.change_form_text("firstname", contact.firstname)
        self.change_form_text("middlename", contact.middlename)
        self.change_form_text("lastname", contact.lastname)
        self.change_form_text("nickname", contact.nickname)
        self.change_form_text("company", contact.company)
        self.change_form_text("address", contact.address)
        self.change_form_text("home", contact.homephone)
        self.change_form_text("mobile", contact.mobilephone)
        self.change_form_text("work", contact.workphone)
        self.change_form_text("email", contact.email1)
        self.change_form_text("email2", contact.email2)
        self.change_form_text("email3", contact.email3)
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

    def open_to_edit_contact_by_index(self, index):
        wd = self.app.driver
        time.sleep(2)
        self.open_home_page()
        wd.find_elements(By.CSS_SELECTOR, "td:nth-child(8) > a > img")[index].click()

    def open_to_edit_contact_by_id(self, id):
        wd = self.app.driver
        time.sleep(2)
        self.open_home_page()
        wd.find_element(By.CSS_SELECTOR, "a[href='edit.php?id=%s']" % id).click()

    def edit_first(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.driver
        self.open_to_edit_contact_by_index(index)
        self.fill_form(contact)
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(74)").click()
        self.return_to_homepage()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.driver
        self.open_to_edit_contact_by_id(id)
        self.fill_form(contact)
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(74)").click()
        self.return_to_homepage()
        self.contact_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.driver
        time.sleep(2)
        self.open_home_page()
        wd.find_elements(By.CSS_SELECTOR, "td:nth-child(7) > a > img")[index].click()

    def get_contacts_from_view_page(self, index):
        wd = self.app.driver
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        homephone = re.search('H: (.*)', text).group(1)
        mobilephone = re.search('M: (.*)', text).group(1)
        workphone = re.search('W: (.*)', text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone)

    def create(self, contact):
        wd = self.app.driver
        self.open_home_page()
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_form(contact)
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(75)").click()
        wd.implicitly_wait(4)
        self.return_to_homepage()
        wd.implicitly_wait(4)
        self.contact_cache = None

    def delete_first(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.driver
        self.select_contact_by_index(index)
        wd.find_element(By.XPATH, "//*[@id='content']/form[2]/div[2]/input").click()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.driver
        self.select_contact_by_id(id)
        wd.find_element(By.XPATH, "//*[@id='content']/form[2]/div[2]/input").click()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.driver
        wd.find_element(By.NAME, "selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.driver
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.driver
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.driver
            self.open_home_page()
            self.contact_cache = []
            el_index = 2  # запись начинается со второй строки в таблице
            for element in wd.find_elements(By.NAME, "entry"):
                text_first = element.find_element(By.XPATH, ("//*[@id='maintable']/tbody/tr[" + str(el_index) +
                                                             "]/td[3]")).text
                text_last = element.find_element(By.XPATH, ("//*[@id='maintable']/tbody/tr[" + str(el_index) +
                                                            "]/td[2]")).text
                contact_id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                address = element.find_element(By.XPATH, ("//*[@id='maintable']/tbody/tr[" + str(el_index) +
                                                          "]/td[4]")).text
                all_phones = element.find_element(By.CSS_SELECTOR, "td:nth-child(6)").text
                all_emails = element.find_element(By.CSS_SELECTOR, "td:nth-child(5)").text
                self.contact_cache.append(Contact(firstname=text_first, lastname=text_last, id=contact_id,
                                                  all_phones_on_home_page=all_phones,
                                                  all_emails_on_home_page=all_emails,
                                                  address=address))
                el_index += 1
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.driver
        self.open_to_edit_contact_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        mobilephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        email1 = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                       email1=email1, email2=email2, email3=email3, address=address)
